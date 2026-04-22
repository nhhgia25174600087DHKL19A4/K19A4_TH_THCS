
a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a.append(x)

n = len(a)
b = []

for i in range(n):
    if a[i] > 0:
        b.append(a[i])

for i in range(n):
    if a[i] <= 0:
        b.append(a[i])

print("Danh sách sau khi đưa số dương lên đầu:", b)

# b
m = int(input("Nhập số m: "))

a_dau = []
a_dau.append(m)
for i in range(n):
    a_dau.append(a[i])
print("Chèn vào đầu:", a_dau)

a_cuoi = []
for i in range(n):
    a_cuoi.append(a[i])
a_cuoi.append(m)
print("Chèn vào cuối:", a_cuoi)

a_vt5 = []
for i in range(n):
    if i == 4:
        a_vt5.append(m)
    a_vt5.append(a[i])

if n < 5:
    a_vt5.append(m)

print("Chèn vào vị trí thứ 5:", a_vt5)