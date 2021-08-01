#@author: sareeliu
#@date: 2021/5/28 21:06
import asyncio

async def func(val):
    print("开始执行func【"+str(val)+"】函数")
    await asyncio.sleep(int(val))
    print("执行func【"+str(val)+"】函数结束")

async def main():
    print("进入main函数")
    f1 = asyncio.create_task(func(3))
    f2 = asyncio.create_task(func(6))
    await f1
    await f2
    print("退出main函数")

asyncio.run(main())