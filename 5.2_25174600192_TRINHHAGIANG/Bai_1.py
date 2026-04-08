n = int(input("Nhập số phần tử: "))

a = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    a.append(x)

# a
tong = 0
for x in a:
    tong = tong + x
print("Tổng các phần tử:", tong)

# b
dem_duong = 0
tong_duong = 0
for x in a:
    if x > 0:
        dem_duong = dem_duong + 1
        tong_duong = tong_duong + x

print("Số phần tử dương:", dem_duong)
print("Tổng các số dương:", tong_duong)

# c
vi_tri_am = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am = i
        break

print("Vị trí số âm đầu tiên:", vi_tri_am)

# d
vi_tri_duong = -1
for i in range(len(a)):
    if a[i] > 0:
        vi_tri_duong = i

print("Vị trí số dương cuối cùng:", vi_tri_duong)

# e
max_value = a[0]
vi_tri_max = 0

for i in range(len(a)):
    if a[i] >= max_value:
        max_value = a[i]
        vi_tri_max = i

print("Giá trị lớn nhất:", max_value)
print("Vị trí cuối của max:", vi_tri_max)