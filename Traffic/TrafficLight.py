from random import randrange
from Traffic.TrafficStatus import TrafficStatus

class TrafficLight:
    time = 0.0

    def __init__(self, P, Q, W):
        self.constraints = []
        self.solveValue = 0
        self.priority = P
        self.quantity = Q
        self.weight = W

        self.status = TrafficStatus.RED

        self.time = 0.0
        self.minGreen = 3.5
        self.minOrange = 3.5
        self.minRed = 2.0
        self.minClearWay = 6.0

        self.blocking = False
        self.needsToBeOn = False

    def getScore(self):
        return self.priority * self.quantity * self.weight

    def update(self, t):
        self.time += t
        # Rood naar Groen
        if self.status is TrafficStatus.RED and self.time >= self.minRed and not self.blocking and self.solveValue > 0.0:
            self.status = TrafficStatus.GREEN
            self.time = 0.0
        # Groen naar oranje
        if self.status is TrafficStatus.GREEN and self.time >= self.minGreen and self.solveValue <= 0.0:
            self.status = TrafficStatus.ORANGE
            self.time = 0.0
        # Oranje naar rood
        if self.status is TrafficStatus.ORANGE and self.time >= self.minOrange:
            self.status = TrafficStatus.RED
            self.time = 0.0
        # Groen/oranje moet nog aanblijven
        if (self.status is TrafficStatus.GREEN and self.time <= self.minGreen) or (self.status is TrafficStatus.ORANGE and self.time <= self.minOrange):
            self.needsToBeOn = True
        else:
            self.needsToBeOn = False
        # Rood ontruimingstijd nog bezig
        if self.status is TrafficStatus.RED and self.time < self.minClearWay:
            self.blocking = True
        else:
            self.blocking = False
        # Verhoog weights voor verkeer dat al langer staat te wachten
        if self.status is TrafficStatus.RED and self.quantity > 0:
            self.weight += 0.05
        else:
            self.weight = 1.0