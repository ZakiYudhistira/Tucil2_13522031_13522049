import Point
import numpy as np
import Display
import matplotlib.pyplot as plt
import time
import math as mt

class BezierCurve:
    def __init__(self, Iterate) -> None:
        # Attributes assignment
        self.points = [] # Anchor points
        self.count = 0
        self.nIteration = Iterate
        self.results = [] # Result points

    def add(self, point : Point):
        """
        Add a point into the anchor points array
        """
        self.count += 1
        self.points.append(point)

    def addSol(self, point : Point):
        """
        Add a point into the result array
        """
        self.results.append(point)

    def clearResults(self):
        """
        Delete result points
        """
        self.results = []

    def createCurve(self, brute : bool):
        """
        Bezier curve generation algorithm
        """
        print(f"Depth : {self.nIteration}")
        if brute:
            # Using the bruteforce approach
            start = time.time()
            print(">> Using the BRUTEFORCE approach <<")
            increment = 1 / (2**self.nIteration)
            # n depth increment
            t = float(0)
            while(t <= 1):
                temp = Point.Point(0,0)
                n = len(self.points) - 1
                for i in range(len(self.points)):
                    # Bezier sum formula
                    temp += mt.comb(n,i)*((1-t)**(n-i))*(t**i)*self.points[i]
                t += increment
                self.addSol(temp)
                # bezier point addition to the result array
            end = time.time()
            print(">> BRUTEFORCE Runtime : ", end="")
            print((end - start) * 1000, "ms")
        else:
            # Using the divide and conquer approach
            start = time.time()
            print(">> Using the DIVIDE AND CONQUER approach <<")
            self.addSol(self.points[0])
            # first anchor point addition
            for i in range(len(self.points)-2):
                self.createCurveDnc(self.nIteration, self.points[0+i], self.points[1+i], self.points[2+i])
            self.addSol(self.points[len(self.points)-1])
            end = time.time()
            print(">> DIVIDE AND CONQUER Runtime : ", end="")
            print((end - start) * 1000, "ms")
        print(">> Displaying Curve... <<")
        return end - start

    def createCurveDnc(self, Iterations : int, p0 : Point, p1 : Point, p2 : Point):
        """
        Using the divide and conquer approach in the bezier curve generation
        """
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
        """
        To print each anchor point coordinate in the bezier curve
        """
        for x in self.points:
            x.printCoordinate()

    def printResult(self):
        """
        To print each result point coordinate in the bezier curve
        """
        for x in self.results:
            x.printCoordinate()

    def displayCurve(self):
        """
        Bezier curve render
        """
        for point in self.points:
            Display.plotDot(point.x, point.y)
        Display.plotLine(self.points)
        Display.plotLine(self.results)
        plt.show()

main = BezierCurve(15)
main.add(Point.Point(-2,-8))
main.add(Point.Point(2,2))
main.add(Point.Point(6,5))
main.createCurve(True)
main.displayCurve()
# main.printResult()


