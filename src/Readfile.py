import Point
path = "test/"

def readFile():
    result = []
    file_name = input("Enter file name: ")
    try:
        with open(path + file_name, "r") as file_points:
            n_inputs = int(file_points.readline())
            for _ in range(n_inputs):
                x, y = map(int, file_points.readline().split())
                result.append(Point.Point(x, y))
    except FileNotFoundError:
        print("File doesn't exist, terminating program...")
        exit()
    return result