base = input("Enter the banner base: ")
repeat = int(input("Enter the number of repeats: "))
text = input("Enter the text: ")

banner = base * repeat
banner_len = len(banner)
txt_len = len(text)

if txt_len <= banner_len: # Center the text over the banner
    space = banner_len - txt_len
    indent = space // 2

    print(" " * indent + text)
    print(banner)
else: # Center the banner under the text
    space = txt_len - banner_len
    indent = space // 2
    print(text)
    print(" " * indent + banner)
