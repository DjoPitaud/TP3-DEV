import asyncio

async def count_to_ten():
    for i in range(1, 11): 
        print(i)
        await asyncio.sleep(0.5)  


async def main():
    tasks = [count_to_ten(), count_to_ten() ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
