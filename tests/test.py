from smartg4f import async_get_provider, get_provider
import asyncio

async def test():
    try:
        print("Async client:")
        await async_get_provider(log=True, timeout=1)
        print("Sync client")
        get_provider(log=True)
        print("Test succeded")
    except Exception as e:
        print("Test failed: ", e)

asyncio.run(test())