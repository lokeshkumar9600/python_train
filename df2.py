"""
A scientific report is been generated in US English and it has to be converted to Indian English. Some words have to be changed as per the given format
Color -> colour
In some words the letter “z” have to be replaced with “s” like synchronize to synchronise

Read the document and convert it to Indian English

"""
x = input()
if "z" in x:
    x = x.replace("z","s")
    print(x)

