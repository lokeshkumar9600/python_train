y = input()

if len(y) != 10:
    print("invalid")
elif not y[0:2].isalpha() :
    print("invlaid")
elif not y[2:4].isdigit():
    print("invalid")
elif not y[4:6].isalpha():
    print("invalid")
elif not y[6::].isdigit():
    print("invalid")
else:
    print("valid")