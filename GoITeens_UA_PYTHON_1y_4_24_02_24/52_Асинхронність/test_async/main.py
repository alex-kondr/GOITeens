import time
import asyncio


start = time.time()


def do_something(i):
    print(f"Старт чудової програми № {i}...")
    time.sleep(5)
    print(f"Програма № {i} закінчила свою роботу.")


async def do_something_async(i):
    print(f"Старт чудової програми № {i}...")
    await asyncio.sleep(5)
    print(f"Програма № {i} закінчила свою роботу.")
    return f"Задача № {i}"


# for i in range(10):
#     do_something(i)


async def main():
    tasks = []
    for i in range(10):
        tasks.append(do_something_async(i))

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


asyncio.run(main())

end = time.time()
print(f"Код працював {end - start} с")