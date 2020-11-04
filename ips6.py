
# x = input()
# y = x[0:4]
# count_upper = 0 
# for i in list(y):
#     if i.isupper():
#         count_upper += 1
    
# if count_upper >= 2 :
#     print(x.upper())
# else:
#     print(x)

# x = input().split(",")
# x.sort()
# print(x)

"""
Write a Python program to find the first appearance of the substring 'Yes' and 'Good' from a given string, if 'Yes' follows the 'Good', replace the whole 'yes'...'Good' substring with 'better'. Return the resulting string.

Sample String : 'Yes the description looks Good!'
'The description looks Good!'
Expected Result : 'The lyrics is good!'
'The lyrics is better!'

Input: Get the input string, s, entered by user

Output:Display the result string s1


"""
s = input()
s = s.lower()
if  "yes" in s and "good" in s:
    s = s.split()
    if s.index("yes") < s.index("good"):
        s.remove("yes")
        print(" ".join(s))
    else:
        pass
elif "good" in s :
        print(s.replace("good","better"))