n = int(input("Nhập số lượng phần tử n: "))
a = []
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(val)
#a
if len(a) < 2:
    print("Danh sách cần ít nhất 2 phần tử để tìm số lớn thứ hai.")
else:
    
    max1 = a[0]
    for x in a:
        if x > max1:
            max1 = x
    
    max2 = None
    vi_tri_max2 = -1
    for i in range(len(a)):
        if a[i] != max1:
            if max2 is None or a[i] > max2:
                max2 = a[i]
                vi_tri_max2 = i
    
    if max2 is not None:
        print(f"Giá trị lớn thứ hai là {max2} tại vị trí {vi_tri_max2}")
    else:
        print("Không có giá trị lớn thứ hai (tất cả phần tử bằng nhau).")

# b
max_lien_tiep = 0
current_lien_tiep = 0
for x in a:
    if x > 0:
        current_lien_tiep += 1
        if current_lien_tiep > max_lien_tiep:
            max_lien_tiep = current_lien_tiep
    else:
        current_lien_tiep = 0
print("Số lượng số dương liên tiếp nhiều nhất:", max_lien_tiep)

# c
max_tong = 0
current_tong = 0
count_max_tong = 0
current_count = 0

for x in a:
    if x > 0:
        current_tong += x
        current_count += 1
        if current_tong > max_tong:
            max_tong = current_tong
            count_max_tong = current_count
    else:
        current_tong = 0
        current_count = 0
print(f"Số lượng số dương liên tiếp có tổng lớn nhất ({max_tong}) là: {count_max_tong}")