import re
x = input()
if re.match('^[a-zA-z0-9]*$', x):
    print("valid")
else:
    print("invalid")