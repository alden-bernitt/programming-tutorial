num = int(input("Enter an integer: "))

parity = "odd"
if num % 2 == 0:
    parity = "even"

print(num, "is " + parity)
