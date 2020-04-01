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

async def solve(sleepTime):
    solver.solve()
    if crossroad.update(sleepTime):
        await socket.send(crossroad.getJson())
        
    #clear()
    crossroad.print()

#TODO: Handle websocket data
async def main():
    await websockets.serve(socket.receive, "localhost", 8000)._create_server()

    while True:
        sleepTime = 1
        await solve(sleepTime)
        await asyncio.sleep(sleepTime)
        
loop = asyncio.new_event_loop()
try:
    loop.create_task(main())
    loop.run_forever()
finally:
    loop.close()

print("done")