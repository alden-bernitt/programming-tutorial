num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# num1 will hold the smallest integer, num2 will hold the middle integer,
# and num3 will hold the largest integer.

if num2 < num1:
    temp = num1
    num1 = num2
    num2 = temp

if num3 < num1:
    temp = num1
    num1 = num3
    num3 = temp

if num3 < num2:
    temp = num2
    num2 = num3
    num3 = temp

print(num1, num2, num3)
