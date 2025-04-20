import time
import asyncio


start_time = time.time()


def do_something(i):
    print(f"Старт програми № '{i}'...")
    time.sleep(1.5)
    print(f"Програма № '{i}' завершила свою роботу")


async def do_something_async(i):
    print(f"Старт програми № '{i}'...")
    await asyncio.sleep(1.5)
    print(f"Програма № '{i}' завершила свою роботу.")
    return i


# for i in range(10):
#     do_something(i)

for i in range(10):
    asyncio.run(do_something_async(i))

end_time = time.time()
print(f"Програма тривала {end_time - start_time} c")

# async def main():
#     tasks = []
#     for i in range(10):
#         tasks.append(do_something_async(i))

#     return await asyncio.gather(*tasks)


# if __name__ == "__main__":
#     end_tasks = asyncio.run(main())

#     print(f"{end_tasks}")
