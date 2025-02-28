# SmartG4F
View on [GitHub](https://github.com/grandguyjs/smartg4f)

A python package that selects g4f providers for you.

Use `pip install smartg4f` to install the package

Instead of supplying a provider, enter `get_provider()`.
This function will validate each g4f provider and return a RetryProvider list

## Synchronous client

Note: With the synchronous client, you cannot set a custom timeout!

```
import g4f
from smartg4f import get_provider

response = g4f.ChatCompletion.create(
    model=model,
    provider=get_provider(),
    messages=messages,
)
```

```
get_provider(
    prompt: String #Prompt that tests the providers (Default: "Say hello")
    validation: Function #Validation function (Default: returns True if the output is of type str)
    model: ModelType #(Default: gpt-4o)
    log: Boolean #Log providers
)

# Example usage
get_provider(
    prompt="How is the weather today?",
    model="gpt-4",
    log=False,
)
```

## Asynchronous client

```
import g4f
from smartg4f import async_get_provider

response = g4f.ChatCompletion.create(
    model=model,
    provider=await async_get_provider(),
    messages=messages,
)
```

```
async_get_provider(
    prompt: String #Prompt that tests the providers (Default: "Say hello")
    validation: Function #Validation function (Default: returns True if the output is of type str)
    model: ModelType #(Default: gpt-4o)
    timeout: Integer #When a provider is too slow (Default: 15 seconds)
    log: Boolean #Log providers
)

# Example usage
await async_get_provider(
    prompt="How is the weather today?",
    model="gpt-4",
    timeout=5,
    log=False,
)
```

## Troubleshooting
1. Use `await async_get_provider(*args)` and `get_provider(*args)`
2. If you use the `await async_get_provider()` method **inside** a function, you need async.
3. If you use the `await async_get_provider()` method **outside** a function, you need `asyncio.run()`.
4. Make sure you have **g4f** installed