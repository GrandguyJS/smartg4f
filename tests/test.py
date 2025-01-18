from smartg4f import get_fastest_providers
import asyncio

async def test():
    await get_fastest_providers()

asyncio.run(test())