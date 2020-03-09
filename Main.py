from Crossroad import Crossroad
from Solver import Solver
import time

crossroad = Crossroad()
solver = Solver(crossroad)
solver.solve()
solver.print()

#TODO: Handle websocket data

while (crossroad.totalTraffic() > 0):
    crossroad.update()
    solver.solve()#updates solveValue in each trafficLight
    solver.print()
    time.sleep(0.5)

print("done")