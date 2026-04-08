danh_sach = []
print("Nhập các số nguyên (Nhập 0 để dừng lại):")
while True:
    so = int(input("Nhập số: "))
    if so == 0:
        break
    danh_sach.append(so)
ds_duong = []
ds_am = []
for x in danh_sach:
    if x > 0:
        ds_duong.append(x)
    else:
        ds_am.append(x)
danh_sach_moi = ds_duong + ds_am
print("\na. Danh sách sau khi đưa số dương lên đầu:", danh_sach_moi)
m = int(input("\nNhập số m cần chèn: "))
danh_sach_moi = [m] + danh_sach_moi
danh_sach_moi = danh_sach_moi + [m]
if len(danh_sach_moi) >= 5:
    nua_dau = danh_sach_moi[:4]
    nua_sau = danh_sach_moi[4:]
    danh_sach_moi = nua_dau + [m] + nua_sau
    print(f"b. Danh sách sau khi chèn {m} vào đầu, cuối và vị trí thứ 5:")
else:
    print(f"b. Danh sách sau khi chèn {m} vào đầu và cuối (không đủ 5 phần tử):")
print(danh_sach_moi)