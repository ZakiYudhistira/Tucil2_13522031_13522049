import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs')
# plt.plot(t, t**3, 'g^')
# plt.show()

import BezierCurve as Bc
import Display as Dis

A = Bc.BezierCurve()

P0 = Bc.Point(0,0)
P1 = Bc.Point(1,1)
P2 = Bc.Point(2,0)

A.points.append(P0)
A.points.append(P1)
A.points.append(P2)

plt.plot(A.points[0].x, A.points[0].y, 'ro', A.points)
plt.show()