#//trafic.azurewebsites.net/controller #//echo.websocket.org/
import json
import websockets
import asyncio
from Crossroads.Crossroad import Crossroad 

class Socket:
    def __init__(self, crossroad):
        self.crossroad = crossroad
        
    def isValidJson(self, message):
        x = {"A1":1,"A2":1,"A3":1,"A4":1,"AB1":1,"AB2":1,
             "B1":1,"B2":1,"B3":1,"B4":1,"B5":0,"BB1":2,
             "C1":1,"C2":2,"C3":1,"D1":2,"D2":2,"D3":1,
             "E1":1,"EV1":1,"EV2":1,"EV3":1,"EV4":1,
             "FF1":1,"FF2":1,"FV1":1,"FV2":1,"FV3":1,"FV4":1,
             "GF1":1,"GF2":1,"GV1":1,"GV2":1,"GV3":1,"GV4":1}
        obj = json.loads(message) # Convert to json object
        if type(obj) is not type({}): # Check if object is dictionary
            return False
        for i in x: # Check if all lanes of crossroad are stored in object
            if i not in obj:
                return False
        return True

    async def receive(self, websocket, path):
        try:
            async for message in websocket:
                if not message or not message.strip():
                    continue
                message = message.replace("\\r", "")
                message = message.replace("\r", "")
                message = message.replace("\\n", "")
                message = message.replace("\n", "")
                if self.isValidJson(message):
                    print("Received: " + message)
                    self.crossroad.setQuantities(json.loads(message))
                    response = self.crossroad.getJson()
                    if response and response.strip():
                        await websocket.send(response)
                        #print("Response: " + response)
        except:
            print("receive error")