n = int(input("Nhập số lượng phần tử n: "))
a = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(so)
tong = 0
for x in a:
    tong += x
print(f"a. Tổng các phần tử: {tong}")
dem_duong = 0
tong_duong = 0
for x in a:
    if x > 0:
        dem_duong += 1
        tong_duong += x
print(f"b. Có {dem_duong} số dương, tổng là: {tong_duong}")
vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break 
if vi_tri_am_dau != -1:
    print(f"c. Vị trí phần tử âm đầu tiên là: {vi_tri_am_dau}")
else:
    print("c. Không có số âm nào trong danh sách.")
vi_tri_duong_cuoi = -1
for i in range(len(a)):
    if a[i] > 0:
        vi_tri_duong_cuoi = i 
if vi_tri_duong_cuoi != -1:
    print(f"d. Vị trí phần tử dương cuối cùng là: {vi_tri_duong_cuoi}")
else:
    print("d. Không có số dương nào trong danh sách.")
if len(a) > 0:
    max_val = a[0]
    vi_tri_max_cuoi = 0
    for i in range(len(a)):
        if a[i] >= max_val: 
            max_val = a[i]
            vi_tri_max_cuoi = i
    print(f"e. Phần tử lớn nhất là {max_val} tại vị trí {vi_tri_max_cuoi}")