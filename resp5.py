#special sequence 
from re import match
test = "the sun"
if match("\Athe" , test): #here \A matches with the starting of the string
    print("valid")
else:
    print("invalid")