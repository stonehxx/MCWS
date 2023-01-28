import asyncio
import websockets
import SERVER

async def echo(websocket):
    await websocket.send(SERVER.first_send())
    async for message in websocket:
        await websocket.send(SERVER.reception(message))

async def main():
    async with websockets.serve(echo,"192.168.1.11",8080):
        await asyncio.Future()

asyncio.run(main())