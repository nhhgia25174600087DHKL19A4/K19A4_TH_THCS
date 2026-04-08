n = int(input("Nhập số lượng phần tử n: "))
a = []

for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(val)
# a
tong = 0
for x in a:
    tong += x
print("Tổng các phần tử:", tong)
# b
dem_duong = 0
tong_duong = 0
for x in a:
    if x > 0:
        dem_duong += 1
        tong_duong += x
print(f"Số lượng số dương: {dem_duong}, Tổng số dương: {tong_duong}")
# c
vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break
if vi_tri_am_dau != -1:
    print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau)
else:
    print("Không có số âm trong danh sách.")
# d
vi_tri_duong_cuoi = -1
for i in range(len(a) - 1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi = i
        break
if vi_tri_duong_cuoi != -1:
    print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi)
else:
    print("Không có số dương trong danh sách.")

# e
if len(a) > 0:
    max_val = a[0]
    vi_tri_max_cuoi = 0
    for i in range(len(a)):
        if a[i] >= max_val:
            max_val = a[i]
            vi_tri_max_cuoi = i
    print(f"Phần tử lớn nhất: {max_val}, Vị trí cuối cùng của nó: {vi_tri_max_cuoi}")