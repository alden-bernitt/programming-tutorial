banner = "*~.~**~.~**~.~**~.~*"

text = input("Enter the text: ")

space = len(banner) - len(text)
indent = space // 2

print(" " * indent + text)
print(banner)
