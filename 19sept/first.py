def hon_test(x,y,type_of_stud):
    if type_of_stud == "n":
        return x 
    if type_of_stud == "h":
        return x+y

tp =  input("enter the type of degree : ")
cred =  hon_test(160,10,tp)
print(f"{cred} credits are required")