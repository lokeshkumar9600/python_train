from re import match 
x = "apple"
if match("^(a|b).*",x):      #(a|b) here ()is used to group and | is used as an or operator
    print("valid")
else:
    print("invalid")