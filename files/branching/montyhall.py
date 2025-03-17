# Simulate the Monty Hall game.
# Step 1) Hide a prize behind a door.
# Step 2) Prompt the user to select a door.
# Step 3) Tell the player which door the prize is NOT behind
#   (Do not divulge any information about the user's door)
# Step 4) Ask the user if they would like to switch doors.
#   (Then switch the user's door to the other door if they choose to)
# Step 5) Reveal the results to the user.
# NO DATA STRUCTURES ALLOWED.

import random

# Reperesents the door that the prize is behind.
prize = random.randint(1, 3)

# Record the doors with no prize.
if prize == 1:
    noprize1 = 2
    noprize2 = 3
elif prize == 2:
    noprize1 = 1
    noprize2 = 3
else:
    noprize1 = 1
    noprize2 = 2

# Represents the door that the user has selected.
print()
selected = int(input("Choose a door (1, 2, or 3)\n> "))

# Choose a door to reveal; the door should have no prize behind it and should
# be different from the door that the user selected.
# At the same time, record the door that was not revealed and not selected by
# the user.
if selected != noprize1:
    revealed = noprize1
    if selected != noprize2:
        remaining = noprize2
else:
    revealed = noprize2
    if selected != noprize1:
        remaining = noprize1

if selected != prize:
    remaining = prize

print()
print("\tThe prize is not behind door", revealed)
print()

print("Would you like to switch to door", remaining, "(yes or no)")
change = input("> ")

# Change the door to the remaining non-revealed door if the user has opted to.
if change == "yes":
    selected = remaining

# Reveal the results to the user.
print()
print("\tYou have selected door", selected)
print("\tThe prize was behind door", prize)
if selected == prize:
    print("\tYou win!")
else:
    print("\tYou lose!")
print()
