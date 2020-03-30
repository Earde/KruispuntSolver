from Crossroads.Crossroad import Crossroad
from Solving.Solver import Solver
import time
import os

clear = lambda: os.system('cls')

crossroad = Crossroad()
solver = Solver(crossroad)
solver.solve()
solver.print()

#TODO: Handle websocket data

sleepTime = 0.5
while (True):
    clear()
    crossroad.update(sleepTime)
    solver.solve()#updates solveValue in each trafficLight
    solver.print()
    time.sleep(sleepTime)

print("done")