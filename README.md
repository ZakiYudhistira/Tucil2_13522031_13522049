# Tugas Kecil IF2211 | Bezier Curve Generator
## Contributors
| NIM | Name |
| ------ | ------ |
| 13522031 | Zaki Yudhistira Candra |
| 13522049 | Vanson Kurnialim |

## Description

This program generates a bezier curve using both DIVIDE AND CONQUER and BRUTEFORCE approach. The bezier curve formula is used in the BRUTEFORCE approach.

## Requirements
- Python 3.9.X
- Matplotlib Library

## Installation

1. Make sure python is installed and downloaded
2. Enter this command in the terminal to install matplotlib
```sh
pip install matplotlib
```
3. Navigate to the directory of the program and enter the command below :
```sh
python src/main.py
```
4. Provide a file if you want to input the coordinates using a custom file
Note : Follow the file template below :
```
n number of points
X1 Y1
X2 Y2
X3 Y3
X4 Y4
```

## File Structure
```
├───README.md
│
├───doc  
│   ├─── Tucil_13522031_13522039.pdf
│                      
├───src                                              
    ├─── BezierCurve.py
    ├─── Display.py
    ├─── main.py
    ├─── Point.py
    ├─── Readfile.py
├───test
    ├─── points.txt
    ├─── points1.txt
```