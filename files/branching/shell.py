import random

pea = random.randint(1, 3)
guess = int(input("Which shell is hiding the pea? (Enter 1, 2, or 3): "))

if guess == pea:
    print("You win!")
else:
    print("You lose! The pea was under shell", pea)
