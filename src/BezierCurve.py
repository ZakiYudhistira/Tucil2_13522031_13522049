import Point
import numpy as np
import Display
import matplotlib.pyplot as plt
import time
import math as mt

# Bezier Curve generationn algorithm and class

class BezierCurve:
    def __init__(self, Iterate) -> None:
        # Attributes assignment
        self.points = [] # Anchor points
        self.nIteration = Iterate
        self.results = [] # Result points
        self.proses = []

    def add(self, point : Point):
        """
        Add a point into the anchor points array
        """
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
            # Calling the recursive function
            self.createCurvenDnc(self.nIteration, self.points)
            self.addSol(self.points[len(self.points)-1])
            end = time.time()
            print(">> DIVIDE AND CONQUER Runtime : ", end="")
            print((end - start) * 1000, "ms")
        print(">> Displaying Curve... <<")
        return end - start

    def findMidpoint(self, list_of_points, anchor) :
        """
        To return a midpoint between 2 points
        """
        if (len(list_of_points) == 1) :
            return list_of_points[0]
        else :
            midpoints = [] 
            for i in range(len(list_of_points) - 1) :
                middle = (list_of_points[0+i] + list_of_points[1+i])/2
                midpoints.append(middle)
            if (len(midpoints) > 1) :
                anchor.append(midpoints[0])
                anchor.append(midpoints[-1])
            return self.findMidpoint(midpoints, anchor)

    def createCurvenDnc(self, Iterations, list_of_points) :
        """
        Bezier curve divide and conquer approach
        """
        if (Iterations == 0) :
            pass
        else :
            anchor = []
            middle = self.findMidpoint(list_of_points, anchor)
            leftlist = [list_of_points[0]]
            rightlist = [list_of_points[-1]]
            for i in range(len(anchor)) :
                if (i % 2 == 0) :
                    leftlist.append(anchor[i])
                else :
                    rightlist.insert(0,anchor[i])
            leftlist.append(middle)
            rightlist.insert(0,middle)            

            self.createCurvenDnc(Iterations-1, leftlist)
            self.addSol(middle)
            self.createCurvenDnc(Iterations-1, rightlist)

            # saving iteration points for process visualization
            for i in range(1, len(rightlist)) :
                leftlist.append(rightlist[i])
            self.proses.append(leftlist)

    # def createCurveDnc(self, Iterations : int, p0 : Point, p1 : Point, p2 : Point):
    #     """
    #     Using the divide and conquer approach in the bezier curve generation
    #     """
    #     if Iterations == 0:
    #         pass
    #     else:
    #         midPoint0 = (p0 + p1)/2
    #         midPoint1 = (p1 + p2)/2
    #         midPoint2 = (midPoint0 + midPoint1)/2
    #         self.createCurveDnc(Iterations-1, p0, midPoint0, midPoint2)
    #         self.addSol(midPoint2)
    #         self.createCurveDnc(Iterations-1, midPoint2, midPoint1, p2)

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

    def displayCurve(self, show):
        """
        Bezier curve render
        """
        Display.plotDotLine(self.points)
        Display.plotLine(self.points)
        if (show) :
            Display.plotLineArray(self.proses)
        Display.plotLine(self.results)
        plt.show()

# main = BezierCurve(18)
# main.add(Point.Point(25,0))
# main.add(Point.Point(0,25))
# main.add(Point.Point(13,40))
# main.add(Point.Point(25,30))
# main.add(Point.Point(38,40))
# main.add(Point.Point(50,25))
# main.add(Point.Point(25,0))
# # main.add(Point.Point(-2,-9))
# # main.add(Point.Point(-9,0))
# # main.add(Point.Point(8,-8))
# main.createCurve(False)
# main.displayCurve()
# # main.printResult()


