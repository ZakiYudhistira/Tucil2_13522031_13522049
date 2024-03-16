import BezierCurve as Bc
import Point

try :
    print("\n    || Welcome to the Bezier Curve Generator ||")
    print("|| Developed by : Zaki Yudhistira and Vanson Kurnialim ||\n")
    # print("====================================================")
    print("=--------------------------------------------------=\n")
    # Welcome message

    iterations = int(input("Input the number of iterations : "))
    if (iterations < 1) :
        print(exception)
    main = Bc.BezierCurve(iterations)
    # n iteration inputs / depth

    n = int(input("Input the number of points : "))

    for i in range(n) :
        print(f"Point {i+1}")
        x = float(input("Enter x coordinate : "))
        y = float(input("Enter y coordinate : "))
        main.add(Point.Point(x,y))

    Brute = -1
    while (Brute == -1) :
        confirmation = str(input("Using BruteForce method? (Y/N) : "))
        if (confirmation == "y" or confirmation == "Y") :
            Brute = True
        elif (confirmation == "n" or confirmation == "N") :
            Brute = False 
        else :
            print("Wrong input, try again!")
        
except :
    print("Input invalid, the program will terminate...")

else :
    print("\n")
    main.createCurve(Brute)
    main.displayCurve()
