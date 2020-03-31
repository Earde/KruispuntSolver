from Traffic.TrafficLight import TrafficLight
from Traffic.TrafficPriority import TrafficPriority
import json

class Crossroad:
    #traffic light dictionary
    lights = {}
    #list of names for dictionary keys
    lightNames = ["a1", "a2", "a3", "a4", "ab1", "ab2", "b1", "b2", "b3", "b4", "b5",
                    "bb1", "c1", "c2", "c3", "d1", "d2", "d3", "ev1", "ev2", "ev3", "ev4",
                    "ef1", "ef2", "fv1", "fv2", "fv3", "fv4", "ff1", "ff2", "gv1", "gv2",
                    "gv3", "gv4", "gf1" , "gf2"]

    def __init__(self):
        #create traffic lights
        for i in range(len(self.lightNames)):
            self.lights[self.lightNames[i]] = TrafficLight(1.0, 0.0, 1.0)
        #constraints of each traffic light
        self.lights["a1"].constraints = ["bb1", "b2", "b3", "b4", "b5", "c1", "c2", "d1", 
                                    "d2", "gv1", "gv2", "gf1", "gf2", "fv1", "fv2", "fv3", 
                                    "fv4", "ff1", "ff2"]
        self.lights["a2"].constraints = ["ab1", "b1", "c1", "c2", "ev4", "ef1", "ef2", "gv1", 
                                    "gv2", "gf1", "gf2"]
        self.lights["a3"].constraints = ["ab1", "b1", "c1", "c2", "c3", "d1", "d2", "ev3", 
                                    "ev4", "ef1", "ef2", "gv1", "gv2", "gf1", "gf2"]
        self.lights["a4"].constraints = ["ab1", "ab2", "b1", "d2", "gv1", "gv2", "gf1", "gf2"]
        self.lights["ab1"].constraints = ["a2", "a3", "a4", "b1", "c1", "c2", "c3", "d1", "d2", 
                                        "ev3", "ev4", "ef1", "ef2", "gv1", "gv2", "gf1", "gf2"]
        self.lights["ab2"].constraints = ["a4", "b1", "d2", "gv1", "gv2", "gf1", "gf2"]
        self.lights["b1"].constraints = ["a2", "a3", "a4", "ab1", "ab2", "c1", "c2", "d1", 
                                    "d2", "ev1", "ev2", "ef1", "ef2"]
        self.lights["b2"].constraints = ["a1", "c1", "c2", "d1", "d2", "d3", "ev1", "ev2", 
                                    "ef1", "ef2", "gv3", "gv4", "gf1", "gf2"]
        self.lights["b3"].constraints = ["a1", "c1", "c2", "d1", "d2", "d3", "ev1", "ev2", 
                                    "ef1", "ef2", "gv3", "gv4", "gf1", "gf2"]
        self.lights["b4"].constraints = ["a1", "b5", "bb1", "c2", "ev1", "ev2", "ef1", "ef2", 
                                    "fv3", "fv4", "ff1", "ff2"]
        self.lights["bb1"].constraints = ["a1", "b4", "c2", "d1", "d2", "d3", "ev1", "ev2", 
                                    "ef1", "ef2", "gv3", "gv4", "gf1", "gf2"]
        self.lights["c1"].constraints = ["a1", "a2", "a3", "ab1", "b1", "b2", "b3", "d2", 
                                    "d3", "gv3", "gv4", "gf1", "gf2"]
        self.lights["c2"].constraints = ["a1", "a2", "a3", "ab1", "b1", "b2", "b3", "b4", 
                                    "b5", "bb1", "d1", "fv3", "fv4", "ff1", "ff2"]
        self.lights["c3"].constraints = ["a2", "a3", "ab1", "d1", "ev3", "ev4", "ef1", "ef2"]
        self.lights["d1"].constraints = ["a1", "a2", "a3", "ab1", "b1", "b2", "b3", "bb1", 
                                    "c2", "c3", "ev3", "ev4", "ef1", "ef2", "fv1", "fv2", 
                                    "ff1", "ff2"]
        self.lights["d2"].constraints = ["a1", "a2", "a3", "ab1", "ab2", "b1", "b2", "b3", "bb1", 
                                    "c1", "ev3", "ev4", "ef1", "ef2", "fv1", "fv2", "ff1", "ff2"]
        self.lights["d3"].constraints = ["b2", "b3", "bb1", "c1", "fv1", "fv2", "ff1", "ff2", 
                                    "gv3", "gv4", "gf1", "gf2"]
        self.lights["ev1"].constraints = ["b1", "b2", "b3", "b4", "bb1"]
        self.lights["ev2"].constraints = ["b1", "b2", "b3", "b4", "bb1"]
        self.lights["ev3"].constraints = ["a2", "a3", "ab1", "c3", "d1"]
        self.lights["ev4"].constraints = ["a2", "a3", "ab1", "c3", "d1"]
        self.lights["ef1"].constraints = ["a2", "a3", "ab1", "b1", "b2", "b3", "b4", "bb1", "c3", "d1"]
        self.lights["ef2"].constraints = ["a2", "a3", "ab1", "b1", "b2", "b3", "b4", "bb1", "c3", "d1"]
        self.lights["fv1"].constraints = ["d1", "d2", "d3"]
        self.lights["fv2"].constraints = ["d1", "d2", "d3"]
        self.lights["fv3"].constraints = ["a1", "b4", "c2"]
        self.lights["fv4"].constraints = ["a1", "b4", "c2"]
        self.lights["ff1"].constraints = ["a1", "b4", "c2", "d1", "d2", "d3"]
        self.lights["ff2"].constraints = ["a1", "b4", "c2", "d1", "d2", "d3"]
        self.lights["gv1"].constraints = ["a1", "a2", "a3", "a4", "ab1", "ab2"]
        self.lights["gv2"].constraints = ["a1", "a2", "a3", "a4", "ab1", "ab2"]
        self.lights["gv3"].constraints = ["b2", "b3", "bb1", "c1", "d3"]
        self.lights["gv4"].constraints = ["b2", "b3", "bb1", "c1", "d3"]
        self.lights["gf1"].constraints = ["a1", "a2", "a3", "a4", "ab1", "ab2", "b2", "b3", 
                                    "bb1", "c1", "d3"]
        self.lights["gf2"].constraints = ["a1", "a2", "a3", "a4", "ab1", "ab2", "b2", "b3", 
                                    "bb1", "c1", "d3"]

        #priorities of each traffic light
        self.lights["a1"].priority = TrafficPriority.CAR
        self.lights["a2"].priority = TrafficPriority.CAR
        self.lights["a3"].priority = TrafficPriority.CAR
        self.lights["a4"].priority = TrafficPriority.CAR
        self.lights["ab1"].priority = TrafficPriority.BUS
        self.lights["ab2"].priority = TrafficPriority.BUS
        self.lights["b1"].priority = TrafficPriority.CAR
        self.lights["b2"].priority = TrafficPriority.CAR
        self.lights["b3"].priority = TrafficPriority.CAR
        self.lights["b4"].priority = TrafficPriority.CAR
        self.lights["bb1"].priority = TrafficPriority.BUS
        self.lights["c1"].priority = TrafficPriority.CAR
        self.lights["c2"].priority = TrafficPriority.CAR
        self.lights["c3"].priority = TrafficPriority.CAR
        self.lights["d1"].priority = TrafficPriority.CAR
        self.lights["d2"].priority = TrafficPriority.CAR
        self.lights["d3"].priority = TrafficPriority.CAR 
        self.lights["ev1"].priority = TrafficPriority.WALK
        self.lights["ev2"].priority = TrafficPriority.WALK
        self.lights["ev3"].priority = TrafficPriority.WALK
        self.lights["ev4"].priority = TrafficPriority.WALK
        self.lights["ef1"].priority = TrafficPriority.CYCLE
        self.lights["ef2"].priority = TrafficPriority.CYCLE
        self.lights["fv1"].priority = TrafficPriority.WALK
        self.lights["fv2"].priority = TrafficPriority.WALK
        self.lights["fv3"].priority = TrafficPriority.WALK
        self.lights["fv4"].priority = TrafficPriority.WALK
        self.lights["ff1"].priority = TrafficPriority.CYCLE
        self.lights["ff2"].priority = TrafficPriority.CYCLE
        self.lights["gv1"].priority = TrafficPriority.WALK
        self.lights["gv2"].priority = TrafficPriority.WALK
        self.lights["gv3"].priority = TrafficPriority.WALK
        self.lights["gv4"].priority = TrafficPriority.WALK
        self.lights["gf1"].priority = TrafficPriority.CYCLE
        self.lights["gf2"].priority = TrafficPriority.CYCLE

    def update(self, t):
        hasChanged = False
        for key in self.lights:
            oldStatus = self.lights[key].status
            self.lights[key].update(t)
            if hasChanged is False and self.lights[key].status is not oldStatus:
                hasChanged = True
        return hasChanged

    def totalTraffic(self):
        c = 0
        for key in self.lights:
            c += self.lights[key].quantity
        return c

    def getJson(self):
        obj = {}
        for key in self.lights:
            obj[key] = self.lights[key].status
        return json.dumps(obj)

    def print(self):
        for key in self.lights:
            print(key +":   " + str(self.lights[key].status))