x = "bchse1234g"
alp = x[0:5]
num = x[5:9]
last_d = x[-1]

if len(x)!= 10:
    print("invalid")
elif not alp.isalpha():
    print("invalid")
elif not num.isdigit():
    print("invalid")
elif not last_d.isalpha():
    print("invalid")
else:
    print("entered string is valid pan number")