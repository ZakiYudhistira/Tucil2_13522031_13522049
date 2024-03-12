class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __mul__(self, k : float):
        return Point(self.x*k, self.y*k)
    
    def __rmul__(self, k):
        return self.__mul__(k)
    
    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __radd__(self, other):
        return self.__add__(other)
    
    def getCoordinate(self):
        return (self.x,self.y)
    
    def printCoordinate(self):
        print("x :", self.x, "y :", self.y)