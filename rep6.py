from re import match
word = "bd$"
if match("\w" , word):
    print("valid ")
else:
    print("invalid")