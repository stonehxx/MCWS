import json
import asyncio
import websockets
import API

async def echo(websocket):
    try:
        print("SERVER: CLIENT IN")
        DATA = ["PlayerMessage"]
        for i in DATA:
            print("MODE: " + i + " START SUCCESSFUL")
            await websocket.send(json.dumps(API.send("subscribe",0,i)))
        async for message in websocket:
            await websocket.send(json.dumps(API.reception(json.loads(message))))
    finally:
        print("SERVER: CLIENT OUT")

async def main():
    async with websockets.serve(echo,"192.168.1.10",8080):
        await asyncio.Future()

print("SERVER: SERVER START SUCCESSFUL")
asyncio.run(main())