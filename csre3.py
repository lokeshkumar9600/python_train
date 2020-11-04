import re
x  = input()
if re.match('^[A-B]{1}[a-b]*$',x):
    print("valid")
else:
    print("invalid")