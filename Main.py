from Crossroads.Crossroad import Crossroad
from Solving.Solver import Solver
from Solving.SolverThread import SolverThread
from Network.Socket import Socket
import time
import asyncio
import websockets
import os

crossroad = Crossroad()
socket = Socket(crossroad)
solver = Solver(crossroad)

solverThread = SolverThread(0.5, solver, crossroad)

try:
    solverThread.start()
    server = websockets.serve(socket.receive, "localhost", 8000)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(server)
    loop.run_forever()
except:
    print("error")
finally:
    print("done")