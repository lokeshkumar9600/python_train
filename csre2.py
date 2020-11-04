import re
x = input()
if re.match('^[a-z]+[_][a-z]*$' , x):
    print("valid")
else:
    print("invalid")