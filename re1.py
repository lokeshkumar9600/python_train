import re
x = input()
y = len(x)

if re.match('^[a-zA-z0-9]*$', x):
    print("valid")
else:
    print("invalid")