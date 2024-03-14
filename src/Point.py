class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __mul__(self, k):
        return Point(self.x*k, self.y*k)
    
    def __rmul__(self, k):
        return self.__mul__(k)
    
    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __radd__(self, other):
        return self.__add__(other)
    
    def __truediv__(self, k):
        return Point(self.x/k, self.y/k)
    
    def __rtruediv__(self,k):
        return self.__truediv__(k)
    
    def __eq__(self, point):
        return self.x == point.x and self.y == point.y
    
    def getMidpoint(k1 ,k2):
        return Point(k1 + k2)/2
    
    def getCoordinate(self):
        return (self.x,self.y)
    
    def printCoordinate(self):
        print("x :", self.x, "y :", self.y)