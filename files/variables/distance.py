import math

x1 = float(input("Enter Tom's X coordinate: "))
y1 = float(input("Enter Tom's Y coordinate: "))
x2 = float(input("Enter Jerry's X coordinate: "))
y2 = float(input("Enter Jerry's Y coordinate: "))

xdist = x2 - x1
ydist = y2 - y1
dist = math.sqrt(xdist * xdist + ydist * ydist)

print("The distance between Tom and Jerry is", dist)
