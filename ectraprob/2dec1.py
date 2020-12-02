"""
a class consists of n students (unique) given the name of students 
and the mark scored by the student write the python code to print the name of student
in alphabetical order who have scored more than class averge

"""
def avg(m):
    average = sum(m)//len(m)
    return average

number_stud = int(input("enter the number of students : "))
stud_mark = {}
for i in range(0,number_stud):
    a,b = input().split(",")
    stud_mark[a] = int(b)

marks = tuple(stud_mark.values()) 
name = list(stud_mark.keys())

av = avg(marks)

for i in name :
    if stud_mark[i] >= av :
        print(i)
