
a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a.append(x)

n = len(a)

# a
chen = [1, 2, 3]


a_dau = []
for i in range(3):
    a_dau.append(chen[i])
for i in range(n):
    a_dau.append(a[i])
print("Chèn đầu:", a_dau)
a_cuoi = []
for i in range(n):
    a_cuoi.append(a[i])
for i in range(3):
    a_cuoi.append(chen[i])
print("Chèn cuối:", a_cuoi)

a_vt5 = []
for i in range(n):
    if i == 4:
        for j in range(3):
            a_vt5.append(chen[j])
    a_vt5.append(a[i])

if n < 5:
    for j in range(3):
        a_vt5.append(chen[j])

print("Chèn vị trí thứ 5:", a_vt5)

# b
k = int(input("Nhập vị trí k cần xóa: "))

a_xoa = []
for i in range(n):
    if i != k:
        a_xoa.append(a[i])

print("Danh sách sau khi xóa:", a_xoa)

# c
a_tang = []
for i in range(n):
    a_tang.append(a[i])

for i in range(n - 1):
    for j in range(i + 1, n):
        if a_tang[i] > a_tang[j]:
            temp = a_tang[i]
            a_tang[i] = a_tang[j]
            a_tang[j] = temp

print("Tăng dần:", a_tang)

a_giam = []
for i in range(n):
    a_giam.append(a[i])

for i in range(n - 1):
    for j in range(i + 1, n):
        if a_giam[i] < a_giam[j]:
            temp = a_giam[i]
            a_giam[i] = a_giam[j]
            a_giam[j] = temp

print("Giảm dần:", a_giam)