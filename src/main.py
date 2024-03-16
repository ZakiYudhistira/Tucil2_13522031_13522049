import BezierCurve as Bc
import Point
import Readfile as Rf

# Main program execution

try :
    print("\n     || Welcome to the Bezier Curve Generator ||")
    print("|| Developed by : Zaki Yudhistira and Vanson Kurnialim ||\n")
    print("=-------------------------------------------------------=\n")
    # Welcome message

    flag = input("Do you want to use a file input (Y/N) ? : ").lower()

    if (flag == "y"):
        print(">> Using file input <<")
        points_temp = Rf.readFile()
        iterations = int(input("Input the number of iterations / depth : "))
        if (iterations < 1) :
        # n iteration inputs / depth
            print("Invalid input, terminating program...")
            exit()
            # error handling, to be caught by exception
        main = Bc.BezierCurve(iterations)
        main.points = points_temp

    elif (flag == "n"):
        iterations = int(input("Input the number of iterations / depth : "))
        if (iterations < 1) :
        # n iteration inputs / depth
            print("Invalid input, terminating program...")
            exit()
        main = Bc.BezierCurve(iterations)

        n = int(input("Input the number of points : "))

        for i in range(n) :
        # points input
            print(f"Point {i+1}")
            x = float(input("Enter x coordinate : "))
            y = float(input("Enter y coordinate : "))
            main.add(Point.Point(x,y))

    else:
        print("Input not recongnized, terminating program...")
        exit()
    
    main.printPoints()

    Brute = -1
    while (Brute == -1) :
        # brute force usage
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
    print("")
    main.createCurve(Brute)
    main.displayCurve()

print("\nEnd of execution...\nThank you for using our program !!!")