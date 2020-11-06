import re
x = input()
if re.match('^hey+',x):
    print("valid")
else:
    print("invalid")