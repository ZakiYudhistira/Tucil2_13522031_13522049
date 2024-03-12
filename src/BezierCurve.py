import Point
import numpy as np
import matplotlib.pyplot as plt

class BezierCurve:
    def __init__(self, Iterate) -> None:
        self.points = []
        self.count = 0
        self.nIteration = Iterate
        self.results = []
    def add(self, point : Point):
        self.count += 1
        self.points.append(point)
    def clearResults(self):
        self.res
    def createCurve(self, brute : bool):
        if brute:
            increment = 1 / (2**self.nIteration)
            t = float(0)
            p0 = self.points[0]
            p1 = self.points[1]
            p2 = self.points[2]
            while(t <= 1):
                q0 = p0*(1-t) + p1*t
                q1 = p1*(1-t) + p2*t
                r0 = (1-t)*q0 + q1*t
                self.results.append(r0)
                t += increment
            else:
                print("ganteng")
    def createCurveDnc(self, Iterations : int, p0 : Point, p1 : Point, p2 : Point):
        if Iterations == 0:
        else:
            


    def printPoints(self):
        for x in self.points:
            x.printCoordinate()
    def printResult(self):
        for x in self.results:
            x.printCoordinate()

main = BezierCurve(2)
main.add(Point.Point(2,2))
main.add(Point.Point(6,5))
main.add(Point.Point(9,3))
main.createCurve(True)
main.printResult()