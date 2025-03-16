country = input("What country are you in (USA or JP)?\n> " )
age = int(input("How old are you?\n> "))

word = ""
if country == "JP" and age < 20 or country == "USA" and age < 21:
    word = "not "
print("You are " + word + "allowed to drink")
