n = int(input("Nhập n: "))
a = []

for i in range(n):
    x = int(input())
    a.append(x)

# a
tong = 0
for i in a:
    tong += i
print("Tổng:", tong)

# b
dem = 0
tong_duong = 0
for i in a:
    if i > 0:
        dem += 1
        tong_duong += i
print("Số dương:", dem)
print("Tổng dương:", tong_duong)

# c
vi_tri_am = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am = i
        break
print("Vị trí âm đầu:", vi_tri_am)

# d
vi_tri_duong = -1
for i in range(len(a)):
    if a[i] > 0:
        vi_tri_duong = i
print("Vị trí dương cuối:", vi_tri_duong)

# e
max_val = a[0]
vi_tri_max = 0
for i in range(len(a)):
    if a[i] >= max_val:
        max_val = a[i]
        vi_tri_max = i
print("Max:", max_val, "vị trí cuối:", vi_tri_max)