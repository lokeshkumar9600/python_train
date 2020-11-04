import re
x = input()
if re.match('.*[A-Za-z0-9_]+$',x):
    print("valid")
else:
    print("invalid")