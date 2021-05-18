from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes([web.get('/', hello)])

web.run_app(app)

# That’s it. Now, head over to http://localhost:8080/ to see the results.