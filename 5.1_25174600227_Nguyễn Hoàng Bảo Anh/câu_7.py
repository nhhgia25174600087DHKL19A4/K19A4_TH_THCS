chuoi = input("Nhập chuỗi: ")
cac_tu = chuoi.split() 
chuoi_chuanhoa = ""

for i in range(len(cac_tu)):
    if i == len(cac_tu) - 1:
        chuoi_chuanhoa = chuoi_chuanhoa + cac_tu[i]
    else:
        chuoi_chuanhoa = chuoi_chuanhoa+ cac_tu[i] + " "

print(f"Chuỗi đã chuẩn hóa: '{chuoi_chuanhoa}'")