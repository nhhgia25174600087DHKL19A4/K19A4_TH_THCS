a = []
while True:
    x = int(input("Nhap so (0 de dung): "))
    if x == 0:
        break
    a.append(x)
print("Danh sach:", a)
#a
x = int(input("Nhap x can tim: "))

for i in range(len(a)):
    if a[i] == x:
        print("Vi tri cua x:", i)
#b
for i in range(len(a)):
    if a[i] == x:
        new = int(input("Nhap gia tri moi: "))
        a[i] = new
        break
print("Danh sach sau khi sua:", a)
#c
y = int(input("Nhap y: "))
vitri = int(input("Nhap vi tri (0-dau, 1-cuoi, 2-giua): "))

if vitri == 0:
    a.insert(0, y)
elif vitri == 1:
    a.append(y)
else:
    a.insert(len(a)//2, y)
print("Danh sach sau khi them:", a)
#d
print("Truoc khi sap xep:", a)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("Sau khi sap xep:", a)  
#e
xoa = int(input("Nhap gia tri can xoa: "))
print("Truoc khi xoa:", a)
for i in range(len(a)):
    if a[i] == xoa:
        a.pop(i)
        break
print("Sau khi xoa:", a)             