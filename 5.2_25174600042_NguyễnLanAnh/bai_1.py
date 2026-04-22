n = int(input("Nhập n: "))
a = []
for i in range(n):
    print("Nhập phần tử thứ ", i, ":")
    so = int(input())
    a.append(so)
#a
tong = 0
for x in a:
    tong = tong + x
print("a, Tổng các phần tử là: ", tong)
#b
dem_so_duong = 0
tong_so_duong = 0
for x in a:
    if x > 0:
        dem_so_duong = dem_so_duong + 1
        tong_so_duong = tong_so_duong + x
print("b, Số lượng số dương: ", dem_so_duong, "- Tổng của chúng: ", tong_so_duong)
#c
vt_am_dau = -1
for i in range(len(a)):
    if a[i] < 0:
        vt_am_dau = i
        break
print("c, Vị trí phần tử âm đầu tiên ", vt_am_dau)
#d
vt_duong_cuoi = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        vt_duong_cuoi = i 
        break
print("d, Vị trí phần tử dương cuối cùng: ", vt_duong_cuoi)
#e
max_val = a[0]
vt_max_cuoi = 0
for i in range(len(a)):
    if a[i] >= max_val:
        max_val = a[i]
        vt_max_cuoi = i
ket_qua = (max_val, vt_max_cuoi)
print("e, Số lớn nhất là: ", ket_qua[0], "tại vị trí cuối cùng là", ket_qua[1])
