import asyncio

import aiomysql


async def main():
    pool = await aiomysql.create_pool(

    )

    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM people;")
            print(await cursor.fetchall())

    pool.close()
    await pool.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())