"""
a school is encouraging their students to participate in olympiad of three subjects maths
physics and chemistry ..they conduct a competetion inside the school and choose top 5 studnts in each of the 
olympiad the school plans to arrange a bus to take them to regional olympiad some of the students 
prefer to come to the center by their own transport given the details find the number of students who need
transport 
"""
print("enter the physics toppers")
stud_lst = {}
for i in range(0,5):
    name,trans = input().split(",")
    stud_lst[name] = trans

print("enter the chemistry toppers")
for i in range(0,5):
    name,trans = input().split(",")
    stud_lst[name] = trans

print("enter the maths toppers")
for i in range(0,5):
    name,trans = input().split(",")
    stud_lst[name] = trans
print("students who need transport")
for j,x in stud_lst.items():
    if x != "self":
        print(j)


