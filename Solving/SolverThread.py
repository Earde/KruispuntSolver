from Crossroads.Crossroad import Crossroad
from Solving.Solver import Solver
from Network.Socket import Socket
import threading
import time
import asyncio
import websockets
import os

class SolverThread (threading.Thread):
    def __init__(self, sleepTime, solver, crossroad, socket):
        threading.Thread.__init__(self)
        self.sleepTime = sleepTime
        self.solver = solver
        self.crossroad = crossroad
        self.socket = socket
        self.clear = lambda: os.system('cls')

    def run(self):
        while True:
            self.solver.solve()
            if self.crossroad.update(self.sleepTime):
                print("update")
                #self.socket.send(self.crossroad.getJson())
        
            #self.clear()
            #self.crossroad.printTraffic()
            time.sleep(self.sleepTime)