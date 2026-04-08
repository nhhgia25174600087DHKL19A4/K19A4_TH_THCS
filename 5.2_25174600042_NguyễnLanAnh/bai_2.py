n = int(input("Nhập số lượng phần tử: "))
a = []
for i in range(n):
    print("Nhập phần tử thứ", i, ":")
    so = int(input())
    a.append(so)
#a
ds_khong_trung = list(set(a)) 
ds_khong_trung.sort(reverse=True) 
if len(ds_khong_trung) < 2:
    print("a. Không có số lớn thứ hai")
else:
    so_lon_nhi = ds_khong_trung[1] 
    vi_tri_nhi = a.index(so_lon_nhi) 
    
    ket_qua_a = (so_lon_nhi, vi_tri_nhi) # Đưa vào tuple
    print("a. Số lớn thứ hai là", ket_qua_a[0], "tại vị trí", ket_qua_a[1])
#b
max_day = 0       
dang_dem = 0      

for x in a:
    if x > 0:
        dang_dem = dang_dem + 1
        if dang_dem > max_day:
            max_day = dang_dem
    else:
        dang_dem = 0
print("b. Số lượng số dương liên tiếp nhiều nhất là:", max_day)
#c
max_tong = 0      
tong_hien_tai = 0 

for x in a:
    if x > 0:
        tong_hien_tai = tong_hien_tai + x
        if tong_hien_tai > max_tong:
            max_tong = tong_hien_tai
    else:
         tong_hien_tai = 0
print("c. Tổng số dương liên tiếp lớn nhất là:", max_tong)