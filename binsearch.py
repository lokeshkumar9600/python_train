# def binsearch(arr,item):
#     first  = 0 ; 
#     last = len(arr)-1
#     found =  False
#     while(first <= last and not found):
#         mid = (first+last)//2
#         if arr[mid] == item:
#             found = True
#         else:
#             if item < arr[mid]:
#                 last = mid-1
#             else:
#                 first = mid + 1
    
#     return found
def binary_search(item_list,item):
    item_list.sort()
    first = 0
    last = len(item_list)-1
    found = False
    while( first<=last and not found):
	    mid = (first + last)//2
	    if item_list[mid] == item :
		    found = True
	    else:
		    if item < item_list[mid]:
			    last = mid - 1
		    else:
			    first = mid + 1	
    return found
print(binary_search([3,2,6,8,1],1))

# def binary_search(item_list,item):
#     item.sort()
# 	first = 0
# 	last = len(item_list)-1
# 	found = False
# 	while( first<=last and not found):
# 		mid = (first + last)//2
# 		if item_list[mid] == item :
# 			found = True
# 		else:
# 			if item < item_list[mid]:
# 				last = mid - 1
# 			else:
# 				first = mid + 1	
# 	return found
	
# print(binary_search([3,2,6,8,8], 2))
