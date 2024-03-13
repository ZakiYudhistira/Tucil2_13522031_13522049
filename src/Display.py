import matplotlib.pyplot as plt
    
def plotDot(x, y) :
    plt.plot(x, y, 'ro')

def plotLine(list_of_dot) :
    x = []
    y = []
    for i in range(len(list_of_dot)) :
        x.append(list_of_dot[i].x)
        y.append(list_of_dot[i].y)
    plt.plot(x, y)