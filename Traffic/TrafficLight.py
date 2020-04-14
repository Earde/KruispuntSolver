from random import randrange
from Traffic.TrafficStatus import TrafficStatus

class TrafficLight:
    constraints = []
    solveValue = 0

    status = TrafficStatus.RED

    minGreen = 3.5
    minOrange = 3.5
    minRed = 2.0
    minClearWay = 6.0

    blocking = False #kijkt of er nog ontruimt moet worden
    needsToBeOn = False

    time = 0.0

    def __init__(self, P, Q, W):
        self.priority = P
        self.quantity = Q
        self.weight = W

    def getScore(self):
        return self.priority * self.quantity * self.weight

    def update(self, t):
        self.time += t
        # Rood naar Groen
        if self.status is TrafficStatus.RED and self.time >= self.minClearWay and self.solveValue > 0.0:
            self.status = TrafficStatus.GREEN
            self.time = 0.0
        # Groen/oranje moet aanblijven
        if (self.status is TrafficStatus.GREEN and self.time < self.minGreen) or (self.status is TrafficStatus.ORANGE and self.time < self.minOrange):
            self.needsToBeOn = True
        else:
            self.needsToBeOn = False
        # Groen naar oranje
        if self.status is TrafficStatus.GREEN and self.time >= self.minGreen and self.solveValue <= 0.0:
            self.status = TrafficStatus.ORANGE
            self.time = 0.0
        # Oranje naar rood
        if self.status is TrafficStatus.ORANGE and self.time >= self.minOrange:
            self.status = TrafficStatus.RED
            self.time = 0.0
        # Rood ontruimingstijd klaar
        if self.status is TrafficStatus.RED and self.time < self.minClearWay:
            blocking = True
        # Rood ontruimingstijd nog bezig
        else:
            self.blocking = False

        if self.status is TrafficStatus.RED and self.quantity > 0:
            self.weight += 0.01 * self.quantity
        else:
            self.weight = 1.0

    def fakeTraffic(self):
        #add fake traffic
        if (randrange(30) == 10):
            self.quantity += 1
        #resolve fake traffic
        if self.status is TrafficStatus.GREEN and self.quantity > 0:
            self.quantity -= 1