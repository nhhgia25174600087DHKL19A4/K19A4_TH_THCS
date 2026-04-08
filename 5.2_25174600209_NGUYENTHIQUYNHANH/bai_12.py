password = input("Nhập mật khẩu để kiểm tra: ")
co_chu_thuong = False
co_chu_hoa = False
co_chu_so = False
co_ky_tu_dac_biet = False
chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chu_so = "0123456789"
ky_tu_dac_biet = "$#@"
do_dai = len(password)
hop_le = True
if do_dai < 6 or do_dai > 12:
    print("- Lỗi: Độ dài phải từ 6 đến 12 ký tự.")
    hop_le = False
for ky_tu in password:
    if ky_tu in chu_thuong:
        co_chu_thuong = True
    elif ky_tu in chu_so:
        co_chu_so = True
    elif ky_tu in chu_hoa:
        co_chu_hoa = True
    elif ky_tu in ky_tu_dac_biet:
        co_ky_tu_dac_biet = True
if co_chu_thuong == False:
    print("- Lỗi: Thiếu ít nhất 1 chữ cái thường [a-z].")
    hop_le = False
if co_chu_so == False:
    print("- Lỗi: Thiếu ít nhất 1 con số [0-9].")
    hop_le = False
if co_chu_hoa == False:
    print("- Lỗi: Thiếu ít nhất 1 chữ cái hoa [A-Z].")
    hop_le = False
if co_ky_tu_dac_biet == False:
    print("- Lỗi: Thiếu ít nhất 1 ký tự đặc biệt [$#@].")
    hop_le = False
if hop_le == True:
    print("\n=> Mật khẩu HỢP LỆ!")
else:
    print("\n=> Mật khẩu KHÔNG HỢP LỆ. Em sửa lại nhé em yêu!")