from pulp import *
from Crossroads.Crossroad import Crossroad

class Solver:
    crossroad = None

    def __init__(self, cr):
        self.crossroad = cr

    def addConstraint(self, p, t, l, r):
        p += t[l] + t[r] <= 1

    def needsToBeOrangeOrGreen(self, p, val, trafficStatus):
        if (trafficStatus > 1):
            trafficStatus = 1
        p += val >= trafficStatus

    def solve(self):
        #variables
        tls = LpVariable.dicts("vars", self.crossroad.lightNames, 0, 1, cat='Integer')

        #constraints
        problem = LpProblem("trafficLight", LpMaximize)

        for key in self.crossroad.lights:
            self.needsToBeOrangeOrGreen(problem, tls[key], self.crossroad.lights[key].status)
            for i in range(len(self.crossroad.lights[key].constraints)):
                self.addConstraint(problem, tls, key, self.crossroad.lights[key].constraints[i])

        objective = None
        #optimization function
        for i in range (len(tls)):
            objective += tls[self.crossroad.lightNames[i]] * self.crossroad.lights[self.crossroad.lightNames[i]].getScore()
        problem += objective
        problem.solve()
        for key in self.crossroad.lights:
            self.crossroad.lights[key].solveValue = tls[key].varValue

    def print(self):
        #print(problem)
        #print(objective)
        for key in self.crossroad.lights:
            print(key +":   " + str(self.crossroad.lights[key].status))