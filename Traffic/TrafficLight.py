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

        self.time = 0.0 # Lopende tijd in secondes
        # Minimale tijden
        self.minGreen = 3.5
        self.minOrange = 3.5
        self.minRed = 2.0
        self.minClearWay = 6.0

        self.blocking = False

    def getScore(self):
        return self.priority * self.quantity * self.weight

    def update(self, t, canGoGreen):
        self.time += t
        # Groen naar oranje
        if self.status is TrafficStatus.GREEN and self.time >= self.minGreen and self.solveValue <= 0.0:
            self.status = TrafficStatus.ORANGE
            self.time = 0.0
        # Oranje naar rood
        if self.status is TrafficStatus.ORANGE and self.time >= self.minOrange:
            self.status = TrafficStatus.RED
            self.time = 0.0
        # Rood naar Groen
        if canGoGreen and self.status is TrafficStatus.RED and self.time >= self.minRed and self.solveValue >= 1.0:
            self.status = TrafficStatus.GREEN
            self.time = 0.0
        # Kijk of het stoplicht blokkerend is voor andere stoplichten
        if self.status is TrafficStatus.GREEN or self.status is TrafficStatus.ORANGE or (self.status is TrafficStatus.RED and self.time < self.minClearWay):
            self.blocking = True
        else:
            self.blocking = False
        # Zet weights
        if self.status is TrafficStatus.RED and self.quantity > 0: # Verhoog weights voor verkeer dat al langer staat te wachten
            self.weight += 0.05
        elif self.status is TrafficStatus.GREEN and self.quantity > 0: # Verlaag weights voor als het stoplicht op groen staat
            self.weight -= 0.10
        else: # Reset weights als er geen verkeer meer staat of naar oranje gaat
            self.weight = 1.0
        if self.weight < 1.0:
            self.weight = 1.0