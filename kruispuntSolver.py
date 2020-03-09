from pulp import *

class TrafficLight:
    constraints = []
    def __init__(self, P, Q, W):
        self.priority = P
        self.quantity = Q
        self.weight = W

    def GetScore(self):
        return self.priority * self.quantity * self.weight

def addConstraint(p, t, l, r):
    p += t[l] + t[r] <= 1

lights = {}
lightNames = ["a1", "a2", "a3", "a4", "ab1", "ab2", "b1", "b2", "b3", "b4", "b5",
"bb1", "c1", "c2", "c3", "d1", "d2", "d3", "ev1", "ev2", "ev3", "ev4",
"ef1", "ef2", "fv1", "fv2", "fv3", "fv4", "ff1", "ff2", "gv1", "gv2",
"gv3", "gv4", "gf1" , "gf2"]

for i in range(len(lightNames)):
    lights[lightNames[i]] = TrafficLight(1.0, 1.0, 1.0)

lights["a1"].constraints = ["bb1", "b2", "b3", "b4", "b5", "c1", "c2", "d1", 
                          "d2", "gv1", "gv2", "gf1", "gf2", "fv1", "fv2", "fv3", 
                          "fv4", "ff1", "ff2"]
lights["a2"].constraints = ["ab1", "b1", "c1", "c2", "ev4", "ef1", "ef2", "gv1", 
                          "gv2", "gf1", "gf2"]
lights["a3"].constraints = ["ab1", "b1", "c1", "c2", "c3", "d1", "d2", "ev3", 
                          "ev4", "ef1", "ef2", "gv1", "gv2", "gf1", "gf2"]
lights["a4"].constraints = ["ab1", "ab2", "b1", "d2", "gv1", "gv2", "gf1", "gf2"]
lights["ab1"].constraints = ["a2", "a3", "a4", "b1", "c1", "c2", "c3", "d1", "d2", 
                             "ev3", "ev4", "ef1", "ef2", "gv1", "gv2", "gf1", "gf2"]
lights["ab2"].constraints = ["a4", "b1", "d2", "gv1", "gv2", "gf1", "gf2"]
lights["b1"].constraints = ["a2", "a3", "a4", "ab1", "ab2", "c1", "c2", "d1", 
                          "d2", "ev1", "ev2", "ef1", "ef2"]
lights["b2"].constraints = ["a1", "c1", "c2", "d1", "d2", "d3", "ev1", "ev2", 
                          "ef1", "ef2", "gv3", "gv4", "gf1", "gf2"]
lights["b3"].constraints = ["a1", "c1", "c2", "d1", "d2", "d3", "ev1", "ev2", 
                          "ef1", "ef2", "gv3", "gv4", "gf1", "gf2"]
lights["b4"].constraints = ["a1", "b5", "bb1", "c2", "ev1", "ev2", "ef1", "ef2", 
                          "fv3", "fv4", "ff1", "ff2"]
lights["bb1"].constraints = ["a1", "b4", "c2", "d1", "d2", "d3", "ev1", "ev2", 
                           "ef1", "ef2", "gv3", "gv4", "gf1", "gf2"]
lights["c1"].constraints = ["a1", "a2", "a3", "ab1", "b1", "b2", "b3", "d2", 
                          "d3", "gv3", "gv4", "gf1", "gf2"]
lights["c2"].constraints = ["a1", "a2", "a3", "ab1", "b1", "b2", "b3", "b4", 
                          "b5", "bb1", "d1", "fv3", "fv4", "ff1", "ff2"]
lights["c3"].constraints = ["a2", "a3", "ab1", "d1", "ev3", "ev4", "ef1", "ef2"]
lights["d1"].constraints = ["a1", "a2", "a3", "ab1", "b1", "b2", "b3", "bb1", 
                          "c2", "c3", "ev3", "ev4", "ef1", "ef2", "fv1", "fv2", 
                          "ff1", "ff2"]
lights["d2"].constraints = ["a1", "a2", "a3", "ab1", "ab2", "b1", "b2", "b3", "bb1", 
                            "c1", "ev3", "ev4", "ef1", "ef2", "fv1", "fv2", "ff1", "ff2"]
lights["d3"].constraints = ["b2", "b3", "bb1", "c1", "fv1", "fv2", "ff1", "ff2", 
                          "gv3", "gv4", "gf1", "gf2"]
lights["ev1"].constraints = ["b1", "b2", "b3", "b4", "bb1"]
lights["ev2"].constraints = ["b1", "b2", "b3", "b4", "bb1"]
lights["ev3"].constraints = ["a2", "a3", "ab1", "c3", "d1"]
lights["ev4"].constraints = ["a2", "a3", "ab1", "c3", "d1"]
lights["ef1"].constraints = ["a2", "a3", "ab1", "b1", "b2", "b3", "b4", "bb1", "c3", "d1"]
lights["ef2"].constraints = ["a2", "a3", "ab1", "b1", "b2", "b3", "b4", "bb1", "c3", "d1"]
lights["fv1"].constraints = ["d1", "d2", "d3"]
lights["fv2"].constraints = ["d1", "d2", "d3"]
lights["fv3"].constraints = ["a1", "b4", "c2"]
lights["fv4"].constraints = ["a1", "b4", "c2"]
lights["ff1"].constraints = ["a1", "b4", "c2", "d1", "d2", "d3"]
lights["ff2"].constraints = ["a1", "b4", "c2", "d1", "d2", "d3"]
lights["gv1"].constraints = ["a1", "a2", "a3", "a4", "ab1", "ab2"]
lights["gv2"].constraints = ["a1", "a2", "a3", "a4", "ab1", "ab2"]
lights["gv3"].constraints = ["b2", "b3", "bb1", "c1", "d3"]
lights["gv4"].constraints = ["b2", "b3", "bb1", "c1", "d3"]
lights["gf1"].constraints = ["a1", "a2", "a3", "a4", "ab1", "ab2", "b2", "b3", 
                           "bb1", "c1", "d3"]
lights["gf2"].constraints = ["a1", "a2", "a3", "a4", "ab1", "ab2", "b2", "b3", 
                           "bb1", "c1", "d3"]
#variables
tls = LpVariable.dicts("vars", lightNames, 0, 1, cat='Integer')

#constraints
problem = LpProblem("trafficLight", LpMaximize)

for key in lights:
    for i in range(len(lights[key].constraints)):
        addConstraint(problem, tls, key, lights[key].constraints[i])

objective = None
#optimization function
for i in range (len(tls)):
    objective += tls[lightNames[i]] * lights[lightNames[i]].GetScore()
problem += objective
problem.solve()

print(problem)
#print(objective)
for i in range (len(lightNames)): 
    print(lightNames[i] +":   " + str(tls[lightNames[i]].varValue))