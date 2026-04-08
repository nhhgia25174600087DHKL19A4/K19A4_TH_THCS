n = int(input("Nhập số lượng phần tử n: "))
a = []
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(val)
# a.
if len(a) < 2:
    print("Danh sách cần ít nhất 2 phần tử")
else:
    max_1 = a[0]
    for x in a:
        if x > max_1:
            max_1 = x
    max_2 = None
    vi_tri_max_2 = -1
    for i in range(len(a)):
        if a[i] != max_1:
            if max_2 is None or a[i] > max_2:
                max_2 = a[i]
                vi_tri_max_2 = i
    if max_2 is None:
        print("Không có số lớn thứ hai (tất cả các số bằng nhau)")
    else:
        print(f"Số lớn thứ hai là {max_2} tại vị trí {vi_tri_max_2}")
# b.
max_lien_tiep = 0
dem_hien_tai = 0
for x in a:
    if x > 0:
        dem_hien_tai += 1
    else:
        if dem_hien_tai > max_lien_tiep:
            max_lien_tiep = dem_hien_tai
        dem_hien_tai = 0
if dem_hien_tai > max_lien_tiep:
    max_lien_tiep = dem_hien_tai
print("Số lượng số dương liên tiếp nhiều nhất:", max_lien_tiep)
# c.
max_tong_lien_tiep = 0
so_luong_cua_max_tong = 0
tong_hien_tai = 0
dem_hien_tai = 0
for x in a:
    if x > 0:
        tong_hien_tai += x
        dem_hien_tai += 1
    else:
        if tong_hien_tai > max_tong_lien_tiep:
            max_tong_lien_tiep = tong_hien_tai
            so_luong_cua_max_tong = dem_hien_tai
        tong_hien_tai = 0
        dem_hien_tai = 0
if tong_hien_tai > max_tong_lien_tiep:
    max_tong_lien_tiep = tong_hien_tai
    so_luong_cua_max_tong = dem_hien_tai
print("Số lượng phần tử trong chuỗi dương có tổng lớn nhất:", so_luong_cua_max_tong)