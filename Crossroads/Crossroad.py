from Traffic.TrafficLight import TrafficLight
from Traffic.TrafficPriority import TrafficPriority
import json

class Crossroad:
    #traffic light dictionary
    lights = {}
    #list of names for dictionary keys
    lightNames = ["A1", "A2", "A3", "A4", "AB1", "AB2", "B1", "B2", "B3", "B4", "B5",
                    "BB1", "C1", "C2", "C3", "D1", "D2", "D3", "EV1", "EV2", "EV3", "EV4",
                    "E1", "FV1", "FV2", "FV3", "FV4", "FF1", "FF2", "GV1", "GV2",
                    "GV3", "GV4", "GF1" , "GF2"]

    def __init__(self):
        #create traffic lights
        for i in range(len(self.lightNames)):
            self.lights[self.lightNames[i]] = TrafficLight(1.0, 0.0, 1.0)
        #constraints of each traffic light
        self.lights["A1"].constraints = ["BB1", "B2", "B3", "B4", "B5", "C1", "C2", "D1", 
                                    "D2", "GV1", "GV2", "GF1", "GF2", "FV1", "FV2", "FV3", 
                                    "FV4", "FF1", "FF2"]
        self.lights["A2"].constraints = ["AB1", "B1", "C1", "C2", "EV4", "E1",  "GV1", 
                                    "GV2", "GF1", "GF2"]
        self.lights["A3"].constraints = ["AB1", "B1", "C1", "C2", "C3", "D1", "D2", "EV3", 
                                    "EV4", "E1",  "GV1", "GV2", "GF1", "GF2"]
        self.lights["A4"].constraints = ["AB1", "AB2", "B1", "D2", "GV1", "GV2", "GF1", "GF2"]
        self.lights["AB1"].constraints = ["A2", "A3", "A4", "B1", "C1", "C2", "C3", "D1", "D2", 
                                        "EV3", "EV4", "E1",  "GV1", "GV2", "GF1", "GF2"]
        self.lights["AB2"].constraints = ["A4", "B1", "D2", "GV1", "GV2", "GF1", "GF2"]
        self.lights["B1"].constraints = ["A2", "A3", "A4", "AB1", "AB2", "C1", "C2", "D1", 
                                    "D2", "EV1", "EV2", "E1"]
        self.lights["B2"].constraints = ["A1", "C1", "C2", "D1", "D2", "D3", "EV1", "EV2", 
                                    "E1",  "GV3", "GV4", "GF1", "GF2"]
        self.lights["B3"].constraints = ["A1", "C1", "C2", "D1", "D2", "D3", "EV1", "EV2", 
                                    "E1",  "GV3", "GV4", "GF1", "GF2"]
        self.lights["B4"].constraints = ["A1", "B5", "BB1", "C2", "EV1", "EV2", "E1",  
                                    "FV3", "FV4", "FF1", "FF2"]
        self.lights["BB1"].constraints = ["A1", "B4", "C2", "D1", "D2", "D3", "EV1", "EV2", 
                                    "E1",  "GV3", "GV4", "GF1", "GF2"]
        self.lights["C1"].constraints = ["A1", "A2", "A3", "AB1", "B1", "B2", "B3", "D2", 
                                    "D3", "GV3", "GV4", "GF1", "GF2"]
        self.lights["C2"].constraints = ["A1", "A2", "A3", "AB1", "B1", "B2", "B3", "B4", 
                                    "B5", "BB1", "D1", "FV3", "FV4", "FF1", "FF2"]
        self.lights["C3"].constraints = ["A2", "A3", "AB1", "D1", "EV3", "EV4", "E1"]
        self.lights["D1"].constraints = ["A1", "A2", "A3", "AB1", "B1", "B2", "B3", "BB1", 
                                    "C2", "C3", "EV3", "EV4", "E1",  "FV1", "FV2", 
                                    "FF1", "FF2"]
        self.lights["D2"].constraints = ["A1", "A2", "A3", "AB1", "AB2", "B1", "B2", "B3", "BB1", 
                                    "C1", "EV3", "EV4", "E1",  "FV1", "FV2", "FF1", "FF2"]
        self.lights["D3"].constraints = ["B2", "B3", "BB1", "C1", "FV1", "FV2", "FF1", "FF2", 
                                    "GV3", "GV4", "GF1", "GF2"]
        self.lights["EV1"].constraints = ["B1", "B2", "B3", "B4", "BB1"]
        self.lights["EV2"].constraints = ["B1", "B2", "B3", "B4", "BB1"]
        self.lights["EV3"].constraints = ["A2", "A3", "AB1", "C3", "D1"]
        self.lights["EV4"].constraints = ["A2", "A3", "AB1", "C3", "D1"]
        self.lights["E1"].constraints = ["A2", "A3", "AB1", "B1", "B2", "B3", "B4", "BB1", "C3", "D1"]
        self.lights["FV1"].constraints = ["D1", "D2", "D3"]
        self.lights["FV2"].constraints = ["D1", "D2", "D3"]
        self.lights["FV3"].constraints = ["A1", "B4", "C2"]
        self.lights["FV4"].constraints = ["A1", "B4", "C2"]
        self.lights["FF1"].constraints = ["A1", "B4", "C2", "D1", "D2", "D3"]
        self.lights["FF2"].constraints = ["A1", "B4", "C2", "D1", "D2", "D3"]
        self.lights["GV1"].constraints = ["A1", "A2", "A3", "A4", "AB1", "AB2"]
        self.lights["GV2"].constraints = ["A1", "A2", "A3", "A4", "AB1", "AB2"]
        self.lights["GV3"].constraints = ["B2", "B3", "BB1", "C1", "D3"]
        self.lights["GV4"].constraints = ["B2", "B3", "BB1", "C1", "D3"]
        self.lights["GF1"].constraints = ["A1", "A2", "A3", "A4", "AB1", "AB2", "B2", "B3", 
                                    "BB1", "C1", "D3"]
        self.lights["GF2"].constraints = ["A1", "A2", "A3", "A4", "AB1", "AB2", "B2", "B3", 
                                    "BB1", "C1", "D3"]

        #priorities of each traffic light
        self.lights["A1"].priority = TrafficPriority.CAR
        self.lights["A2"].priority = TrafficPriority.CAR
        self.lights["A3"].priority = TrafficPriority.CAR
        self.lights["A4"].priority = TrafficPriority.CAR
        self.lights["AB1"].priority = TrafficPriority.BUS
        self.lights["AB2"].priority = TrafficPriority.BUS
        self.lights["B1"].priority = TrafficPriority.CAR
        self.lights["B2"].priority = TrafficPriority.CAR
        self.lights["B3"].priority = TrafficPriority.CAR
        self.lights["B4"].priority = TrafficPriority.CAR
        self.lights["BB1"].priority = TrafficPriority.BUS
        self.lights["C1"].priority = TrafficPriority.CAR
        self.lights["C2"].priority = TrafficPriority.CAR
        self.lights["C3"].priority = TrafficPriority.CAR
        self.lights["D1"].priority = TrafficPriority.CAR
        self.lights["D2"].priority = TrafficPriority.CAR
        self.lights["D3"].priority = TrafficPriority.CAR 
        self.lights["EV1"].priority = TrafficPriority.WALK
        self.lights["EV2"].priority = TrafficPriority.WALK
        self.lights["EV3"].priority = TrafficPriority.WALK
        self.lights["EV4"].priority = TrafficPriority.WALK
        self.lights["E1"].priority = TrafficPriority.CYCLE
        self.lights["FV1"].priority = TrafficPriority.WALK
        self.lights["FV2"].priority = TrafficPriority.WALK
        self.lights["FV3"].priority = TrafficPriority.WALK
        self.lights["FV4"].priority = TrafficPriority.WALK
        self.lights["FF1"].priority = TrafficPriority.CYCLE
        self.lights["FF2"].priority = TrafficPriority.CYCLE
        self.lights["GV1"].priority = TrafficPriority.WALK
        self.lights["GV2"].priority = TrafficPriority.WALK
        self.lights["GV3"].priority = TrafficPriority.WALK
        self.lights["GV4"].priority = TrafficPriority.WALK
        self.lights["GF1"].priority = TrafficPriority.CYCLE
        self.lights["GF2"].priority = TrafficPriority.CYCLE

    def update(self, t):
        hasChanged = False
        for key in self.lights:
            oldStatus = self.lights[key].status
            self.lights[key].update(t)
            if not hasChanged and self.lights[key].status is not oldStatus:
                hasChanged = True
        return hasChanged

    def totalTraffic(self):
        c = 0
        for key in self.lights:
            c += self.lights[key].quantity
        return c

    def setQuantities(self, obj):
        for key in obj:
            self.lights[key].quantity = obj[key];
            
    def getJson(self):
        obj = {}
        for key in self.lights:
            obj[key] = self.lights[key].status
        return json.dumps(obj)

    def printStatus(self):
        for key in self.lights:
            print(key +":   " + str(self.lights[key].status))

    def printTraffic(self):
        for key in self.lights:
            print(key +":   " + str(self.lights[key].quantity))