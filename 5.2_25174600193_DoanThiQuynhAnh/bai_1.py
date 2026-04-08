n = int(input("Nhap n: "))
a = []

for i in range(n):
    a.append(int(input("Nhap phan tu: ")))

tong = 0
for i in range(len(a)):
    tong += a[i]

print("Tong =", tong)

for i in range(n):
    a.append(int(input("Nhap phan tu: ")))

dem = 0
tong = 0

for i in range(len(a)):
    if a[i] > 0:
        dem += 1
        tong += a[i]

print("So luong so duong:", dem)
print("Tong so duong:", tong)
for i in range(n):
    a.append(int(input("Nhap phan tu: ")))

vitri = -1

for i in range(len(a)):
    if a[i] < 0:
        vitri = i
        break

print("Vi tri am dau tien:", vitri)

for i in range(n):
    a.append(int(input("Nhap phan tu: ")))

vitri = -1

for i in range(len(a)):
    if a[i] > 0:
        vitri = i

print("Vi tri duong cuoi cung:", vitri)
for i in range(n):
    a.append(int(input("Nhap phan tu: ")))

max_value = a[0]
vitri = 0

for i in range(len(a)):
    if a[i] >= max_value:
        max_value = a[i]
        vitri = i

print("Gia tri lon nhat:", max_value)
print("Vi tri xuat hien cuoi:", vitri)