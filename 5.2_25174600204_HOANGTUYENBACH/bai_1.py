n = int(input("Nhập số phần tử n: "))
a = []
for i in range(n):
    x = int(input(f"Nhập phần tử a[{i}]: "))
    a.append(x)
# a
tong = 0
for i in range(n):
    tong = tong + a[i]

print("Tổng các phần tử:", tong)
# b
dem_duong = 0
tong_duong = 0

for i in range(n):
    if a[i] > 0:
        dem_duong = dem_duong + 1
        tong_duong = tong_duong + a[i]

print("Số lượng số dương:", dem_duong)
print("Tổng các số dương:", tong_duong)
# c
vi_tri_am_dau = -1

for i in range(n):
    if a[i] < 0:
        vi_tri_am_dau = i
        break

print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau)
# d
vi_tri_duong_cuoi = -1

for i in range(n):
    if a[i] > 0:
        vi_tri_duong_cuoi = i

print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi)
# e
max_val = a[0]
vi_tri_max = 0

for i in range(1, n):
    if a[i] >= max_val:
        max_val = a[i]
        vi_tri_max = i

print("Giá trị lớn nhất:", max_val)
print("Vị trí xuất hiện cuối cùng:", vi_tri_max)