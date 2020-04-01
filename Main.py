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
        sleepTime = 1
        solver.solve()
        if crossroad.update(sleepTime):
            await socket.send(crossroad.getJson())
        
        clear()
        crossroad.print()
        await asyncio.sleep(sleepTime)

#TODO: Handle websocket data
async def main():
    server = websockets.serve(socket.receive, "localhost", 8000)

    task = asyncio.Task(solve())
    while True:
        await asyncio.sleep(1)
        
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(main())
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()

print("done")