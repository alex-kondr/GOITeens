from aiohttp import web


async def handle(request):
    return web.Response(text="Hello, aiohttp!")


app = web.Application()
app.router.add_get('/', handle)
# app.router.add


web.run_app(app)
