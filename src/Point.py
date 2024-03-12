class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def getCoordinate(self):
        return (self.x,self.y)
    def printCoordinate(self):
        print("x :", self.x, "y :", self.y)

