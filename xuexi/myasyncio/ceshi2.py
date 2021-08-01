#@author: sareeliu
#@date: 2021/5/28 21:20
import asyncio,aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://vpswp.com/")
        res = await response.text()
