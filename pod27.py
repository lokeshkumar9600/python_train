a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a+b+c+d == 360:
    if a==b==c==d==90:
        print("rectange")
    elif a==c and b==d:
        print("Parallelogram")
    elif a==b==180 or c==d==180:
        print("Trapezium")
    else:
        print("Quadrilateral")
else:
    print("No Quadrilateral")