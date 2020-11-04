import re
x = input()
if re.match('[a-yA-Y]+[zZ]+[A-Ya-y]+$', x):
    print("valid")
else:
    print("invalid")
