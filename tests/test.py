from smartg4f import get_provider
import asyncio

async def test():
    await get_provider(log=True)

asyncio.run(test())