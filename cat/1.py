"""
factorial of a number 
"""

x = int(input())
pro = 1
for i in range(1,x+1):
    pro *= i

print(str(pro))