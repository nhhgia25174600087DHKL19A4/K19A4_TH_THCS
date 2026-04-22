n = int(input("Nhap so luong: "))
a = []

i = 0
while i < n:
    x = int(input("Nhap so: "))
    a = a + [x]
    i = i + 1
print("List:", a)

# a, tim x
x = int(input("Nhap x can tim: "))
i = 0
tim = False
while i < len(a):
    if a[i] == x:
        print("Vi tri:", i)
        tim = True
        break
    i = i + 1
if tim == False:
    print("Khong co")

# b, sua gia tri
if tim == True:
    y = int(input("Nhap gia tri moi: "))
    a[i] = y
print("Sau khi sua:", a)

# c, them phan tu
y = int(input("Nhap y can them: "))
a = a + [y]   
print("Sau khi them:", a)

# d, sap xep giam dan
i = 0
while i < len(a):
    j = i + 1
    while j < len(a):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        j = j + 1
    i = i + 1
print("Sau sap xep:", a)

# e, xoa phan tu
x = int(input("Nhap gia tri can xoa: "))
i = 0
while i < len(a):
    if a[i] == x:
        a = a[:i] + a[i+1:]
        break
    i = i + 1

print("Sau khi xoa:", a)