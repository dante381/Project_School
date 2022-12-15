import asyncio
import websockets
import json

async def test():
    while True:
        async with websockets.connect('wss://0hqif30xkl.execute-api.us-west-2.amazonaws.com/production') as websocket:
            # x=input("Power: ")
            # dic={"action":"system","power":"{}".format(x)}
            #dic={"action":"sendmessage","key":"{}".format(x)}
            message=await websocket.recv()
            print(message)
                        
            
 
asyncio.get_event_loop().run_until_complete(test())
#asyncio.get_event_loop().run_forever()