# brute-force method of printing out three integers in sorted order.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if num1 < num2:
    if num1 < num3: # num1 is the smallest
        if num2 < num3: # num2 is the middle (num3 is the largest)
            print(num1, num2, num3)
        else: # num3 is the middle (num2 is the largest)
            print(num1, num3, num2)
    else: # num3 is the smallest
        if num1 < num2: # num1 is the middle (num2 is the largest)
            print(num3, num1, num2)
        else: # num2 is the middle (num1 is the largest)
            print(num3, num2, num1)
else:
    if num2 < num3: # num2 is the smallest
        if num1 < num3: # num1 is the middle (num3 is the largest)
            print(num2, num1, num3)
        else: # num3 is the middle (num1 is the largest)
            print(num2, num3, num1)
    else: # num3 is the smallest
        if num1 < num2: # num1 is the middle (num2 is the largest)
            print(num3, num1, num2)
        else: # num2 is the middle (num1 is the largest)
            print(num3, num2, num1)
