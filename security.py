word = input("enter the word:").lower()
inc = int(input("enter the inc value  : "))
x = list(word)
fin = []
for i in range(0,len(x)):
    fin.append(chr(ord(x[i]+inc)))

print(fin)

