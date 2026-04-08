chuoi_so = input("Nhập danh sách số nguyên: ")

ds_so = []
for x in chuoi_so.split():
    ds_so = ds_so + [int(x)]

for so in ds_so:
    assert so % 2 == 0, f"Lỗi: Số {so} là số lẻ!"

print("Xác minh thành công: Tất cả các số đều là số chẵn.")