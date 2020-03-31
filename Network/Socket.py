#//trafic.azurewebsites.net/controller #//echo.websocket.org/
import websocket
import json
from websocket import create_connection

class Socket:
    def __init__(self, ip, message):
        self.ip = ip
        self.message = message
        self.result = ""

    def isvalidjson(self, message):
        x = {"A1":1,"A2":1,"A3":1,"A4":1,"AB1":1,"AB2":1,"B1":1,"B2":1,"B3":1,"B4":1,"B5":0,"BB1":2,"C1":1,"C2":2,"C3":1,"D1":2,"D2":2,"D3":1,"E1":1,"E2":0,"EV1":1,"EV2":1,"EV3":1,"EV4":1,"FF1":1,"FF2":1,"FV1":1,"FV2":1,"FV3":1,"FV4":1,"GF1":1,"GF2":1,"GV1":1,"GV2":1,"GV3":1,"GV4":1}
        dictionary = json.loads(message)
        for i in x:
            if i not in dictionary:
                return False
        return True        

    def connect(self):
        #ws = websocket.WebSocket()
        ws.connect("ws:" + self.ip, http_proxy_host="proxy_host_name", http_proxy_port=8000)
        #ws = create_connection("ws:" + self.ip)
        print(self.message)
        ws.send(self.message) 
        self.result =  ws.recv()
        if self.result is not None
            if self.isvalidjson(self.result):
                i = json.dumps(self.result)
                print(i)
                print("Received '%s'" % self.result)        
        ws.close()
        
    def decode(self):
        return self.result

lol = Socket("127.0.0.1", '{"Z1":1,"A2":1,"A3":1,"A4":1,"AB1":1}')
print(lol.isvalidjson('{"A1":1,"A2":1,"A3":1,"A4":1,"AB1":1,"AB2":1,"B1":1,"B2":1,"B3":1,"B4":1,"B5":0,"BB1":2,"C1":1,"C2":2,"C3":1,"D1":2,"D2":2,"D3":1,"E1":1,"E2":0,"EV1":1,"EV2":1,"EV3":1,"EV4":1,"FF1":1,"FF2":1,"FV1":1,"FV2":1,"FV3":1,"FV4":1,"GF1":1,"GF2":1,"GV1":1,"GV2":1,"GV3":1,"GV4":1}'))      
print(lol.isvalidjson('{"A1":1}'))
#connection = Socket("//localhost", '{"A1":1,"A2":1,"A3":1,"A4":1,"AB1":1,"AB2":1,"B1":1,"B2":1,"B3":1,"B4":1,"B5":0,"BB1":2,"C1":1,"C2":2,"C3":1,"D1":2,"D2":2,"D3":1,"E1":1,"E2":0,"EV1":1,"EV2":1,"EV3":1,"EV4":1,"FF1":1,"FF2":1,"FV1":1,"FV2":1,"FV3":1,"FV4":1,"GF1":1,"GF2":1,"GV1":1,"GV2":1,"GV3":1,"GV4":1}')
#connection.connect()