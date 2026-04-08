n = int(input("Nhập số lượng phần tử n: "))
a = []
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(val)
# a.
tong_tat_ca = 0
for x in a:
    tong_tat_ca += x
print("Tổng các phần tử:", tong_tat_ca)
# b.
dem_duong = 0
tong_duong = 0
for x in a:
    if x > 0:
        dem_duong += 1
        tong_duong += x
print(f"Số lượng số dương: {dem_duong}, Tổng số dương: {tong_duong}")
# c.
vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break
print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau)
# d.
vi_tri_duong_cuoi = -1
for i in range(len(a)):
    if a[i] > 0:
        vi_tri_duong_cuoi = i
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi)
# e.
if len(a) > 0:
    max_val = a[0]
    vi_tri_max_cuoi = 0
    for i in range(len(a)):
        if a[i] >= max_val:
            max_val = a[i]
            vi_tri_max_cuoi = i
    print(f"Phần tử lớn nhất là {max_val} tại vị trí {vi_tri_max_cuoi}")