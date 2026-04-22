n = int(input("Nhập độ dài n: "))
a = []
for i in range(n):
    b = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(b)
# a.
tong_ca_dan_sach = sum(a)
print(f"Tổng các phần tử: {tong_ca_dan_sach}")
# b. 
so_luong_duong = 0
tong_duong = 0
for x in a:
    if x > 0:
        so_luong_duong += 1
        tong_duong += x
print(f"Số lượng số dương: {so_luong_duong}, Tổng số dương: {tong_duong}")
# c. 
vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break 
print(f"Vị trí phần tử âm đầu tiên: {vi_tri_am_dau}")
# d. 
vi_tri_duong_cuoi = -1
for i in range(len(a)):
    if a[i] > 0:
        vi_tri_duong_cuoi = i 
print(f"Vị trí phần tử dương cuối cùng: {vi_tri_duong_cuoi}")
# e.
if a:
    max_val = max(a)
    vi_tri_max_cuoi = -1
    for i in range(len(a)):
        if a[i] == max_val:
            vi_tri_max_cuoi = i
    print(f"Phần tử lớn nhất: {max_val}, Vị trí cuối cùng: {vi_tri_max_cuoi}")