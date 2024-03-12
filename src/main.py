import BezierCurve as Bc
import Display as Dis

A = Bc.BezierCurve()

P0 = Bc.Point(0,0)
P1 = Bc.Point(1,1)
P2 = Bc.Point(2,0)

A.points.append(P0)
A.points.append(P1)
A.points.append(P2)

print(A.points[0].x)
