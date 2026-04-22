a = []

# nhap list
while True:
    x = int(input("Nhap so (0 de dung): "))
    if x == 0:
        break
    a.append(x)

print("List ban dau:", a)

# a. tim x
x = int(input("Nhap x can tim: "))
i = 0
while i < len(a):
    if a[i] == x:
        print("Vi tri cua x:", i)
        break
    i = i + 1

# b. sua gia tri
i = 0
while i < len(a):
    if a[i] == x:
        new = int(input("Nhap gia tri moi: "))
        a[i] = new
        break
    i = i + 1

print("Sau khi sua:", a)

# c. them y
y = int(input("Nhap y: "))
a.append(y)
print("Sau khi them:", a)

# d. sap xep giam dan (while)
i = 0
while i < len(a):
    j = i + 1
    while j < len(a):
        if a[i] < a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t
        j = j + 1
    i = i + 1

print("Sau khi sap xep:", a)

# e. xoa 1 phan tu
if len(a) > 0:
    del a[0]

print("Sau khi xoa:", a)