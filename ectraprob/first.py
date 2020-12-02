"""
shopping cart
"""

num1 = int(input("enter the number of items for son's list : "))
sons_list =[]
for i in range(0,num1):
    x = input("enter the item :")
    sons_list.append(x)

num2 = int(input("enter the number of items for daughter's list :"))
daughter_list = []
for j in range(0,num2):
    y = input("enter the item :")
    daughter_list.append(y)

#To find the common items and the remaining in the cart
common =[]
son_mod =[]
temps = sons_list.copy()
for n in sons_list:
    if n in daughter_list:
        common.append(n)
        temps.remove(n)
    else:
        son_mod.append(n)
        
daughters_mod =[]
tempd = daughter_list.copy()
for n in daughter_list:
    if n in sons_list:
        
        tempd.remove(n)
    else:
        daughters_mod.append(n)

print("#common are")
print(common)
print("remaining sons list")
print(temps)
print("remaining daughters list")
print(tempd)


    




