n= int(input("Nhap so luong phan tu: "))
tp = tuple(range(1, n+10))
print("Tuple ban dau:", tp)

le = []

for x in tp:
    if x > 0 and x % 2 != 0:
        le.append(x)

tp_le = tuple(le)

print("Tuple so le:", tp_le)