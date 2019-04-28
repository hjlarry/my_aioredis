import asyncio

from myredis import Redis


async def simple():
    r = Redis(host="localhost", port=6379, db=0)
    await r.set("foo", "bar")
    value = await r.get("foo")
    print(value)


loop = asyncio.get_event_loop()
loop.run_until_complete(simple())
