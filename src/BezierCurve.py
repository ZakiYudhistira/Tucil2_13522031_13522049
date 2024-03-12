class Point :
    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y

class BezierCurve:
    def __init__(self) -> None:
        self.points = []