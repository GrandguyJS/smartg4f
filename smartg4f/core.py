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

async def get_fastest_providers(prompt, validation, model, timeout):
    providers = [provider for provider in g4f.Provider.__providers__ if provider.working]

    working_providers = []

    for provider in providers:
        try:
            async with asyncio.timeout(timeout):
                res = await g4f.ChatCompletion.create_async(
                    model=model,
                    provider=provider,
                    messages=[{"role": "user", "content": prompt}]
                )
                if not validation(res):
                    raise
            working_providers.append(provider)
        except:
            pass

    if len(working_providers) == 0:
        print("Every provider failed!")
    else:
        pass

    # Return a list of all working providers for RetryProviders
    return working_providers

async def get_provider(prompt="Say hello", validation=default_validate, model="gpt-4o", timeout=15):
    # Returns providers
    # Use provider=get_provider()
    providers = await get_fastest_providers(prompt=prompt, validation=validation, model=model, timeout=timeout)
    return RetryProvider(providers, shuffle=False, single_provider_retry=False, max_retries=1)
