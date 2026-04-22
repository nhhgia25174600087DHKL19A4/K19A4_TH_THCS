a = list(map(int, input("nhap list: ").split()))

ok = True

for i in range(len(a)):
    if a[i] % 2 != 0:
        ok = False
        break

if ok == True:
    print("tat ca deu chan")
else:
    print("co so le")
    