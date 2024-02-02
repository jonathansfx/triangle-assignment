# triangle perimeter assignment
import math
x = " "
print ("WELCOME TO THE TRIANGLE PERIMETER PROGRAM")
print ("ENTER THE COORDINATES OF THE VERTICES OF A TRIANGLE...")
#inputs
print(x)
print("VERTEX A")
xa = float(input("enter the x coordinate for vertex A: "))
ya = float(input("enter the y coordinate for vertex A: "))
print(x)
print("VERTEX B")
xb = float(input("enter the x coordinate for vertex B: "))
yb = float(input("enter the y coordinate for vertex B: "))
print(x)
print("VERTEX C")
xc = float(input("enter the x coordinate for vertex C: "))
yc = float(input("enter the y coordinate for vertex C: "))
print(x)

# process
def dist(x1, y1, x2, y2):

    side_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return side_length

ab = dist(xa, ya, xb, yb)
ac = dist(xa, ya, xc, yc)
bc = dist(xc, yc, xb, yb)

# output
print("SIDE LENGTHS & PERIMETER: ")
print("AB: " + str(ab) + ".")
print("AC: " + str(ac) + ".")
print("BC: " + str(bc) + ".")