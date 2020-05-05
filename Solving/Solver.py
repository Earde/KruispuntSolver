from pulp import *
from Crossroads.Crossroad import Crossroad

class Solver:
    crossroad = None

    def __init__(self, cr):
        self.crossroad = cr

    def addConstraint(self, p, t, l, r):
        p += t[l] + t[r] <= 1

    def needsToBeRed(self, p, val, blocking):
        if (blocking):
            p += val <= 0

    def solve(self):
        oldSolvedValues = []
        for l in self.crossroad.lights.values():
            oldSolvedValues.append(l.status)

        # Solver variabelen
        tls = LpVariable.dicts("vars", self.crossroad.lightNames, 0, 1, cat='Integer')

        # Constraints
        problem = LpProblem("trafficLight", LpMaximize)

        for key in self.crossroad.lights:
            # Voeg versperrende wegen constraints toe
            for i in range(len(self.crossroad.lights[key].constraints)):
                self.addConstraint(problem, tls, key, self.crossroad.lights[key].constraints[i])

        objective = None
        # Optimalisatie functie
        for i in range (len(tls)):
            objective += tls[self.crossroad.lightNames[i]] * self.crossroad.lights[self.crossroad.lightNames[i]].getScore()
        problem += objective
        problem.solve()
        # Update ideale waardes naar de stoplichten
        for key in self.crossroad.lights:
            self.crossroad.lights[key].solveValue = tls[key].varValue

        newSolvedValues = []
        for l in self.crossroad.lights.values():
            newSolvedValues.append(l.status)

        if oldSolvedValues is newSolvedValues:
            return False
        return True