lst = []
while True:
    n = int(input("Nhap so (0 dung): "))
    if n == 0:
        break
    lst.append(n)

print("List ban dau:", lst)
#a
x = int(input("Nhap x can tim: "))
tim = False

for i in range(len(lst)):
    if lst[i] == x:
        print("Vi tri cua x la:", i)
        tim = True
        break

if not tim:
    print("Khong tim thay")
#b
if tim:
    moi = int(input("Nhap gia tri moi: "))
    lst[i] = moi
    print("List sau khi sua:", lst)
#c
y = int(input("Nhap y: "))
vitri = int(input("Nhap vi tri chen: "))

lst.insert(vitri, y)

print("List sau khi them:", lst)
#d
print("Truoc khi sap xep:", lst)

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] < lst[j]:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp

print("Sau khi sap xep giam:", lst)
#e
print("Truoc khi xoa:", lst)

xoa = int(input("Nhap gia tri can xoa: "))

for i in range(len(lst)):
    if lst[i] == xoa:
        lst.pop(i)
        break

print("Sau khi xoa:", lst)