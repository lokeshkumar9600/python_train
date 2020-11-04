from re import match
x = input()
if match('[1-9]{2}[A-Z a-z]{3}[1-9]{4}$',x):
    print("valid")
else:
    print("invalid")