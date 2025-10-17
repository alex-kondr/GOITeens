import time
import asyncio
import random


start_time = time.time()


def do_task(i):
    print(f"Стартує задача № {i}")
    time.sleep(5)
    print(f"Задача № {i} завершилась.")


async def do_tast_async(i):
    print(f"Стартує задача № {i}")
    await asyncio.sleep(random.randint(1, 6))
    print(f"Задача № {i} завершилась.")


# for i in range(1, 6):
#     do_task(i)


async def main():
    my_tasks = []
    for i in range(1, 6):
        my_tasks.append(do_tast_async(i))

    await asyncio.gather(*my_tasks)


asyncio.run(main())

print(f"Задачі виконувались на протягом {time.time() - start_time} c")