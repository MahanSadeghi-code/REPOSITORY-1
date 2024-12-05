a = []
b = []

dars = int(input("enter your books"))
for i in range(dars) :
    c = float(input("enter your grades "))
    if c >= 10 :
        a.append(c)
    else :
        b.append(c)

print(a)
print(b)

