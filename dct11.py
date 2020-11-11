# dct1 = {"num" : 1}
# dct2 = {"no" : 2}
# dct1.update(dct2)
# print(dct1)

val = {
    0:"zero",
    1:"one",
    2: "two",
    3:"three",
    4:"four",
    5: "five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"
}
inp  = input()
if inp.isdigit():
    for i in inp :
        print(val[int(i)] , end = " ")
else :
    print("invalid input")