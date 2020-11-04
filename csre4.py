import re
x = input()
word = "hey"
if re.match(word,x):
    print("valid")
else:
    print("invalid")