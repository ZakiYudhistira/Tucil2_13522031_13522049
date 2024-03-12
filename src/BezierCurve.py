import Point
import numpy as np
import Display
import matplotlib.pyplot as plt
import time

class BezierCurve:
    def __init__(self, Iterate) -> None:
        self.points = []
        self.count = 0
        self.nIteration = Iterate
        self.results = []

    def add(self, point : Point):
        self.count += 1
        self.points.append(point)

    def addSol(self, point : Point):
        self.results.append(point)

    def clearResults(self):
        self.res

    def createCurve(self, brute : bool):
        if brute:
            start = time.time()
            print("Brute Force")
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
            end = time.time()
            Display.plotDot(self.points[0].x, self.points[0].y)
            Display.plotDot(self.points[1].x, self.points[1].y)
            Display.plotDot(self.points[2].x, self.points[2].y)
            Display.plotLine(main.points)
            Display.plotLine(main.results)
            plt.show()
            print((end - start) * 1000, "ms")
        else:
            start = time.time()
            print("Divide and Conquer")
            self.addSol(self.points[0])
            self.createCurveDnc(self.nIteration, self.points[0], self.points[1], self.points[2])
            self.addSol(self.points[2])
            end = time.time()
            Display.plotDot(self.points[0].x, self.points[0].y)
            Display.plotDot(self.points[1].x, self.points[1].y)
            Display.plotDot(self.points[2].x, self.points[2].y)
            Display.plotLine(main.points)
            Display.plotLine(main.results)
            plt.show()
            print((end - start) * 1000, "ms")

    def createCurveDnc(self, Iterations : int, p0 : Point, p1 : Point, p2 : Point):
        if Iterations == 0:
            pass
        else:
            midPoint0 = (p0 + p1)/2
            midPoint1 = (p1 + p2)/2
            midPoint2 = (midPoint0 + midPoint1)/2
            self.createCurveDnc(Iterations-1, p0, midPoint0, midPoint2)
            self.addSol(midPoint2)
            self.createCurveDnc(Iterations-1, midPoint2, midPoint1, p2)

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
main.createCurve(False)
# main.printResult()


