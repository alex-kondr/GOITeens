import time
import asyncio

names = []

start = time.time()


def do_something(i):
    print(f"Стартує команда {i}...")
    time.sleep(5)
    print(f"Команда {i} закінчилась!!!")


async def do_something_async(i):
    print(f"Стартує команда {i}...")
    await asyncio.sleep(0.1)
    print(f"Команда {i} закінчилась!!!")


async def main():
    my_tasks = []
    for i in range(10):
        my_tasks.append(do_something_async(i))

    await asyncio.gather(*my_tasks)


asyncio.run(main())

# for i in range(10):
#     do_something(i)


end = time.time()
print(f"Цей код тривав {end - start } с")