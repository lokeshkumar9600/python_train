import re
x  = input()
if re.match('^[A-Z]{1}[a-z]*$',x):
    print("valid")
else:
    print("invalid")