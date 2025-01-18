import asyncio

import g4f
from g4f.Provider import RetryProvider

def default_validate(param):
    try:
        if not type(param.choices[0].message.content) == str:
            return False
        if len(param.choices[0].message.content) == 0:
            return False
        return True
    except:
        return False

async def get_fastest_providers(prompt, validation, model, timeout, log):
    def log_message(*args):
        if log:
            print(*args)
        else:
            pass

    providers = [provider for provider in g4f.Provider.__providers__ if provider.working and not provider.needs_auth]

    working_providers = []

    for provider in providers:
        try:
            log_message("Testing ", provider.__name__, "...")
            async with asyncio.timeout(timeout):
                res = await g4f.ChatCompletion.create_async(
                    model=model,
                    provider=provider,
                    messages=[{"role": "user", "content": prompt}]
                )
                if not validation(res):
                    raise
            working_providers.append(provider)
            log_message(provider.__name__, " working")
        except:
            log_message(provider.__name__, " not working")

    if len(working_providers) == 0:
        print("Every provider failed!")
    else:
        pass

    # Return a list of all working providers for RetryProviders
    return working_providers

async def get_provider(prompt="Say hello", validation=default_validate, model="gpt-4o", timeout=15, log=False):
    # Returns providers
    # Use provider=get_provider()
    providers = await get_fastest_providers(prompt=prompt, validation=validation, model=model, timeout=timeout, log=log)
    return RetryProvider(providers, shuffle=False, single_provider_retry=False, max_retries=1)