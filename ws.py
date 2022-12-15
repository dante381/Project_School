import websockets
import asyncio

async def handler(websocket,path):
    data=await websocket.recv()
    reply=f"data recieved as: {data}"
    await websocket.send(reply)

ss=websockets.serve(handler,"192.168.1.17",8000)

asyncio.get_event_loop().run_until_complete(ss)
asyncio.get_event_loop().run_forever()