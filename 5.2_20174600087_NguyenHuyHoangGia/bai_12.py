mat_khau = input("Nhập mật khẩu để kiểm tra: ")
co_chu_thuong = False
co_chu_hoa = False
co_so = False
co_ky_tu_dac_biet = False
ky_tu_dac_biet = "$#@ "
do_dai = len(mat_khau)
if do_dai < 6 or do_dai > 12:
    print("Mật khẩu không hợp lệ")
else:
    for chu in mat_khau:
        if 'a' <= chu <= 'z':
            co_chu_thuong = True
        elif 'A' <= chu <= 'Z':
            co_chu_hoa = True
        elif '0' <= chu <= '9':
            co_so = True
        elif chu in ky_tu_dac_biet:
            co_ky_tu_dac_biet = True
    if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet:
        print("Mật khẩu hợp lệ")
    else:
        print("Mật khẩu không hợp lệ")