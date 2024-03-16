import matplotlib.pyplot as plt

# Displaying functions

def plotDot(x, y) :
    """
    plot a point
    """
    plt.plot(x, y, 'ro')

def plotDotLine(list_of_dot) :
    """
    plot multiple points from a list of point
    """
    for i in range(len(list_of_dot)) :
        plotDot(list_of_dot[i].x, list_of_dot[i].y)

def plotLine(list_of_dot) :
    """
    plot a line from a list of point
    """
    x = []
    y = []
    for i in range(len(list_of_dot)) :
        x.append(list_of_dot[i].x)
        y.append(list_of_dot[i].y)
    plt.plot(x, y)

def plotLineArray(list_of_line) :
    """
    plot multiple lines with its points from a list of line
    """
    for i in range(len(list_of_line)) :
        # plotDotLine(list_of_line[i])
        plotLine(list_of_line[i])