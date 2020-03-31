from Crossroads.Crossroad import Crossroad
from Solving.Solver import Solver
from Network.Socket import Socket
import time
import os

clear = lambda: os.system('cls')

socket = Socket("127.0.0.1")
socket.connect()

crossroad = Crossroad()
solver = Solver(crossroad)
solver.solve()
solver.print()

#TODO: Handle websocket data

sleepTime = 1.0
while (True):
    clear()

    obj = socket.receive()
    if obj is not None:
        crossroad.setQuantities(obj)

    solver.solve()
    if crossroad.update(sleepTime):
        socket.send(crossroad.getJson())
    
    crossroad.print()
    time.sleep(sleepTime)

socket.close()
print("done")