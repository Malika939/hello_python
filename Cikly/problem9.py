a = -100
b = a
ifc = 0
while a <= 100:
    if a % 13 == 0 and a % 2 == 0:
        print(a, b ** 2)
        ifc = ifc + 1
    a += 1
print(ifc)

ifC2 = 0
while b <= 100:
    if b % 2 == 1:
        ifC2 += 1
        print(b)
    b += 7
print(ifC2)

