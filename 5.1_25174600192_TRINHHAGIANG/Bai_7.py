s = input("Nhập chuỗi: ")

s = s.strip()
ket_qua = ""
truoc_do_la_khoang_trang = False

for ky_tu in s:
    if ky_tu == " ":
        if truoc_do_la_khoang_trang == False:
            ket_qua = ket_qua + ky_tu
        truoc_do_la_khoang_trang = True
    else:
        ket_qua = ket_qua + ky_tu
        truoc_do_la_khoang_trang = False

print("Chuỗi sau khi chuẩn hóa:", ket_qua)