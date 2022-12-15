import asyncio
import websockets
import json

async def test():
    while True:
        async with websockets.connect('wss://0hqif30xkl.execute-api.us-west-2.amazonaws.com/production') as websocket:
            mac=input('MACID: ')
            x=input("Power: ")
            dic={"action":"system","MACID":"{}".format(mac),"power":"{}".format(x)}
            #dic={"action":"sendmessage","key":"{}".format(x)}
            await websocket.send(json.dumps(dic))
            
 
asyncio.get_event_loop().run_until_complete(test())
#asyncio.get_event_loop().run_forever()