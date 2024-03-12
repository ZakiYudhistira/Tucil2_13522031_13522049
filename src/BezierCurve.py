import Point
import numpy as np
import Display
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
    def createCurve(self, brute : bool):
        if brute:
            increment = 1 / (2**self.nIteration)
            t = float(0)
            P1 = self.points[0]
            P2 = self.points[1]
            P3 = self.points[2]
            while(t <= 1):
                Q1 = P1*(1-t) + P2*t
                Q2 = P2*(1-t) + P3*t
                R1 = (1-t)*Q1 + Q2*t
                self.results.append(R1)
                t += increment
            Display.plotDot(P1.x, P1.y)
            Display.plotDot(P2.x, P2.y)
            Display.plotDot(P3.x, P3.y)
            Display.plotLine(main.points)
            Display.plotLine(main.results)
            plt.show()
        else:
            print("ganteng")
    def printPoints(self):
        for x in self.points:
            x.printCoordinate()
    def printResult(self):
        for x in self.results:
            x.printCoordinate()

main = BezierCurve(10)
main.add(Point.Point(2,2))
main.add(Point.Point(6,5))
main.add(Point.Point(9,3))
main.createCurve(True)
main.printResult()

