n = int(input("Nhập n: "))
a = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(so)
if len(a) < 2:
    print("a. Danh sách cần ít nhất 2 phần tử để tìm số lớn thứ hai.")
else:
    max_1 = a[0]
    for x in a:
        if x > max_1:
            max_1 = x
        max_2 = None
    vi_tri_max_2 = -1
    for i in range(len(a)):
        if a[i] < max_1:
            if max_2 is None or a[i] > max_2:
                max_2 = a[i]
                vi_tri_max_2 = i

    if max_2 is not None:
        print(f"a. Phần tử lớn thứ hai là {max_2} tại vị trí {vi_tri_max_2}")
    else:
        print("a. Không có phần tử lớn thứ hai (các số bằng nhau hết).")
max_lien_tiep = 0
dem_hien_tai = 0
for x in a:
    if x > 0:
        dem_hien_tai += 1
        if dem_hien_tai > max_lien_tiep:
            max_lien_tiep = dem_hien_tai
    else:
        dem_hien_tai = 0
print(f"b. Số lượng các số dương liên tiếp nhiều nhất là: {max_lien_tiep}")
max_tong_lien_tiep = 0
tong_hien_tai = 0
so_luong_cua_tong_max = 0
dem_tam = 0
for x in a:
    if x > 0:
        tong_hien_tai += x
        dem_tam += 1
        if tong_hien_tai > max_tong_lien_tiep:
            max_tong_lien_tiep = tong_hien_tai
            so_luong_cua_tong_max = dem_tam
    else:
        tong_hien_tai = 0
        dem_tam = 0
print(f"c. Số lượng các số dương liên tiếp có tổng lớn nhất ({max_tong_lien_tiep}) là: {so_luong_cua_tong_max}")