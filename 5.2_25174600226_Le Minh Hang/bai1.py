n = int(input("Nhap n: "))
a = []

for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

# a. Tổng
tong = 0
for x in a:
    tong += x
print("Tong:", tong)

# b. Đếm số dương + tổng dương
dem = 0
tong_duong = 0
for x in a:
    if x > 0:
        dem += 1
        tong_duong += x
print("So duong:", dem)
print("Tong duong:", tong_duong)

# c. Vị trí âm đầu tiên
vitri = -1
for i in range(len(a)):
    if a[i] < 0:
        vitri = i
        break
print("Vi tri am dau tien:", vitri)

# d. Vị trí dương cuối cùng
vitri = -1
for i in range(len(a)):
    if a[i] > 0:
        vitri = i
print("Vi tri duong cuoi:", vitri)

# e. Max và vị trí cuối
max_val = a[0]
vitri = 0
for i in range(len(a)):
    if a[i] >= max_val:
        max_val = a[i]
        vitri = i
print("Max:", max_val)
print("Vi tri max cuoi:", vitri)

