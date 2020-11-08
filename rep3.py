#using ^ and $
"""
^ in regex is used to match a word to the begining of the string "^a" matches with abc and doesnt match with bca
$ in regex is used to match a word to the end of the string ".*a$" matches with hella and doesnt match with abb 

"""
from re import match 
textstr =  "apple"
if match("^a",textstr):
    print("match")
else : 
    print("doesnt match")

textstr2 = "bba"
if match(".*a$",textstr2):
    print("match")
else :
    print("doesnt match")