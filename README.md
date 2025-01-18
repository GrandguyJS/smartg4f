# SmartG4F
View on [GitHub](https://github.com/grandguyjs/smartg4f)

A python package that selects g4f providers for you.

Use `pip install smartg4f` to install the package

Instead of supplying a provider, enter `await get_provider()`.
This function will validate each g4f provider and return a RetryProvider list

```
import g4f
from smartg4f import get_provider

response = g4f.ChatCompletion.create(
    model=model,
    provider=await get_provider(),
    messages=messages,
)
```

```
get_provider(
    prompt: String #Prompt that tests the providers (Default: "Say hello")
    validation: Function #Validation function (Default: returns True if the output is of type str)
    model: ModelType #(Default: gpt-4o)
    timeout: Integer #When a provider is too slow (Default: 15 seconds)
)
```

Example usage:
`get_provider(prompt="How is the weather today=", model="gpt-4", timeout=5)`

Troubleshooting:
You need to use await -> If you use get_provider in another function, it must be async, else use asyncio.run()