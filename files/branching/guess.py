import random

prompt = "Guess the number: "
win_msg = "Correct! You win!"
low = 1
high = 20
num = random.randint(low, high)

print("I've selected a number between", low, "and", high)

guess = int(input(prompt))

if guess == num:
    print(win_msg)
else:
    if num < guess:
        print("Incorrect! The number is lower than", guess)
    else:
        print("Incorrect! The number is higher than", guess)

    guess = int(input(prompt))

    if guess == num:
        print(win_msg)
    else:
        print("Incorrect! You lose! The number was", num)

