tolerance = int(input("Enter the mother's tolerance as an integer.\n> "))

count = 0

if tolerance == 0:
    print("Mother: Go ask your father.")
else:
    while count <= tolerance:
        print("Child: Why?")
        count += 1
    print("Mother: Because I said so!")
