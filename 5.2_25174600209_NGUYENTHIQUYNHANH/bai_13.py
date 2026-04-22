chuoi_mat_khau = input("Nhập các mật khẩu (cách nhau bởi dấu phẩy): ")
danh_sach_pw = chuoi_mat_khau.split(',')
chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chu_so = "0123456789"
ky_tu_dac_biet = "$#@"
ket_qua = [] 
for pw in danh_sach_pw:
    pw = pw.strip()
    n = len(pw)
    if n >= 6 and n <= 12:
        co_thuong = False
        co_hoa = False
        co_so = False
        co_dac_biet = False
        for ky_tu in pw:
            if ky_tu in chu_thuong:
                co_thuong = True
            elif ky_tu in chu_hoa:
                co_hoa = True
            elif ky_tu in chu_so:
                co_so = True
            elif ky_tu in ky_tu_dac_biet:
                co_dac_biet = True
                if co_thuong and co_hoa and co_so and co_dac_biet:
                 ket_qua.append(pw)
for i in range(len(ket_qua)):
    if i < len(ket_qua) - 1:
        print(ket_qua[i], end=",")
    else:
        print(ket_qua[i])