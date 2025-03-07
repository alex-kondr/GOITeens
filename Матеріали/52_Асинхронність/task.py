# import asyncio
# import time


# start = time.time()

# def do_something(i: int):
#     print(f"Початок {i}-го завдання")
#     time.sleep(5)
#     print(f"Кінець {i}-го завдання")


# # for i in range(10):
# #     do_something(i)


# async def do_async(i: int):
#     print(f"Початок {i}-го завдання")
#     await asyncio.sleep(5)
#     print(f"Кінець {i}-го завдання")


# async def main():
#     tasks = []
#     for i in range(10):
#         tasks.append(do_async(i))

#     await asyncio.gather(*tasks)


# asyncio.run(main())


# end = time.time() - start
# print(f"Всі завдання виконались за {end} с")
# from fastapi import FastAPI
# import uvicorn


# app = FastAPI()

# if __name__ == "__main__":
#     uvicorn.run("task:app", reload=True)

# import asyncio


# async def do_do():
#     print("start 1")
#     await asyncio.sleep(2)
#     print("end 1")
#     print("start 2")
#     await asyncio.sleep(2)
#     print("end 2")


# asyncio.run(do_do())
# asyncio.run(do_do())


# from fastapi import FastAPI, HTTPException
