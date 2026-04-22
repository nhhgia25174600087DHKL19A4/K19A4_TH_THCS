s = input("Nhập chuỗi cần chuẩn hóa: ")
danh_sach_tu = s.split()
chuoi_chuan_hoa = ""
for i in range(len(danh_sach_tu)):
    chuoi_chuan_hoa += danh_sach_tu[i]
    if i < len(danh_sach_tu) - 1:
        chuoi_chuan_hoa += " "
print(f"Chuỗi sau khi chuẩn hóa là: '{chuoi_chuan_hoa}'")