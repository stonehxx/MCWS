import asyncio
import websockets
import SERVER

async def echo(websocket):
    for i in range(SERVER.first_send(0,0)):
        await websocket.send(SERVER.first_send(1,i))
    async for message in websocket:
        print("Client:" + message)

async def main():
    async with websockets.serve(echo,"192.168.1.11",8080):
        await asyncio.Future()

asyncio.run(main())