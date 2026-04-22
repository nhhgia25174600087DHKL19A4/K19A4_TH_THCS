chuoi = input("Nhập chuỗi: ")

# chuỗi không có các khoảng trắng ở đầu và cuối
while chuoi[0] == " ":
    chuoi = chuoi[1:]

# cách nhau đúng một dấu cách
while chuoi[-1] == " ":
    chuoi = chuoi[:-1]

ket_qua = ""
la_khoang_trang = False

for ky_tu in chuoi:
    if ky_tu == " ":
        if not la_khoang_trang:
            ket_qua += ky_tu
        la_khoang_trang = True
    else:
        ket_qua += ky_tu
        la_khoang_trang = False

print(ket_qua)