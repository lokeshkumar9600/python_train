import re
x = input()
if re.match( '.*ing$', x):
    print("valid")
else:
    print("invalid")