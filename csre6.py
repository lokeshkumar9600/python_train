import re
x = input()
if re.match('.*z', x):
    print("valid")
else:
    print("invalid")