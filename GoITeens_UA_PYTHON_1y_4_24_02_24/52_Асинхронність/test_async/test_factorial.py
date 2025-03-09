import asyncio
import time


start = time.time()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


async def factorial_async(n):
    if n == 0:
        return 1
    else:
        return n * await factorial_async(n-1)


async def main():
    tasks = [factorial_async(900) for _ in range(1000)]
    # tasks = [factorial_async(995)] * 1000
    await asyncio.gather(*tasks)



# for _ in range(1000):
#     factorial(995)

asyncio.run(main())

end = time.time() - start
print(f"Програма тривала {end} с")