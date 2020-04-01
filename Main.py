from Crossroads.Crossroad import Crossroad
from Solving.Solver import Solver
from Network.Socket import Socket
import time
import asyncio
import websockets
import os

clear = lambda: os.system('cls')

crossroad = Crossroad()
socket = Socket(crossroad)

solver = Solver(crossroad)
solver.solve()

async def solve():
    while True:
        sleepTime = 1.0
        solver.solve()
        if crossroad.update(sleepTime):
            await socket.send(crossroad.getJson())
            
            
        crossroad.print()
        await asyncio.sleep(sleepTime)

#TODO: Handle websocket data
async def start_server():
    websockets.serve(socket.recieve, "localhost", 8000)
    while True:
        sleepTime = 1.0
        solver.solve()
        if crossroad.update(sleepTime):
            await socket.send(crossroad.getJson())
            
            
        crossroad.print()
        await asyncio.sleep(sleepTime)
        
asyncio.get_event_loop().run_until_complete(start_server())
asyncio.get_event_loop().run_forever()


print("done")
