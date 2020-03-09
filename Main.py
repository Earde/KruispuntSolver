from Crossroad import Crossroad
from Solver import Solver
import time

crossroad = Crossroad()
solver = Solver(crossroad)
solver.solve()
solver.print()

#TODO: Handle websocket data and update crossroad

while (crossroad.totalTraffic() > 0):
    crossroad.update()
    solver.crossroad = crossroad
    solver.solve()
    solver.print()
    time.sleep(1)

print("done")