from random import randrange

class TrafficLight:
    constraints = []
    solveValue = 0
    def __init__(self, P, Q, W):
        self.priority = P
        self.quantity = Q
        self.weight = W

    def getScore(self):
        return self.priority * self.quantity * self.weight

    def update(self):
        if self.quantity > 0:
            self.weight += 0.01 * self.quantity
        else:
            self.weight = 1.0

    def fakeTraffic(self):
        #add fake traffic
        if (randrange(10) == 3):
            self.quantity += 1
        #resolve fake traffic
        if self.solveValue >= 1 and self.quantity > 0:
            self.quantity -= 1