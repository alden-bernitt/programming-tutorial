print("You are trying to access a rated R movie.")

age = int(input("Please enter your age: "))

if age < 17:
    print("Sorry, you are not allowed to view this movie.")
else:
    print("Access granted")
