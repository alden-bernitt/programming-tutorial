option1 = "I'm looking for a warm meal."
option2 = "I'm trying to find a place to rest."
option3 = "I was chased here by a gang of bandits!"
option4 = "Oh you know...just hanging around."

print("Shop Keeper: Welcome traveler! What brings you to our village")

print()
print("1.", option1)
print("2.", option2)
print("3.", option3)
print("4.", option4)
print()

choice = input("> ")

if choice == "1":
    print("Player:", option1)
    print("Shop Keeper: The pub here offers great meals and better company!")
elif choice == "2":
    print("Player:", option2)
    print("Shop Keeper: You'll get a good night's sleep at the inn.")
elif choice == "3":
    print("Player:", option3)
    print("Shop Keeper: Goodness! I'll alert the guards immediately!")
elif choice == "4":
    print("Player:", option4)
    print("Shop Keeper: Ah...would you be interested in buying?")
