ten_nguoi_dung = input("Nhập tên người dùng: ")
mat_khau = input("Nhập mật khẩu: ")

co_chu_thuong = False  # a
co_chu_hoa = False     # c
co_so = False          # b
co_ky_tu_dac_biet = False  # d
do_dai_hop_le = False      # e,f

if 6 <= len(mat_khau) <= 12:
    do_dai_hop_le = True

for ky_tu in mat_khau:
    if ky_tu.islower():
        co_chu_thuong = True
    elif ky_tu.isupper():
        co_chu_hoa = True
    elif ky_tu.isdigit():
        co_so = True
    elif ky_tu in "S#@":
        co_ky_tu_dac_biet = True

if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_dac_biet and do_dai_hop_le:
    print("Mật khẩu hợp lệ!")
else:
    print("Mật khẩu không hợp lệ!")
    if not co_chu_thuong:
        print("- Mật khẩu cần ít nhất 1 chữ cái thường [a-z].")
    if not co_chu_hoa:
        print("- Mật khẩu cần ít nhất 1 chữ cái hoa [A-Z].")
    if not co_so:
        print("- Mật khẩu cần ít nhất 1 số [0-9].")
    if not co_ky_tu_dac_biet:
        print("- Mật khẩu cần ít nhất 1 ký tự đặc biệt [S#@].")
    if not do_dai_hop_le:
        print("- Độ dài mật khẩu phải từ 6 đến 12 ký tự.")