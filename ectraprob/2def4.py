def avg(lst):
    avg = float(sum(lst)/len(lst))
    avg = round(avg,2)
    return avg

num = int(input("enter the number of students : "))
stud_lst = {}
for i in range(1,num+1):
    print(f"student{i}")
    arr = []
    name = input(f"enter the name of student{i} : ")
    regno = input(f"enter registration number of student{i} : ")
    for n in range(0,3):
        marks = int(input("enter the marks :"))
        arr.append(marks)
    stud_lst[f"student{i}"] = [name,regno,arr]



for j in range(1,num+1):
    print(f"student{j}")
    print(avg(tuple(stud_lst[f"student{j}"][2])))