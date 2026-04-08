
tai_khoan = input("Nhap tai khoan: ")
mat_khau = input("Nhap mat khau: ")

co_chu_thuong = False
co_chu_hoa = False
co_so = False
co_ky_tu_db = False

# kiểm tra từng ký tự
for ch in mat_khau:
    if 'a' <= ch <= 'z':
        co_chu_thuong = True
    elif 'A' <= ch <= 'Z':
        co_chu_hoa = True
    elif '0' <= ch <= '9':
        co_so = True
    elif ch == 'S' or ch == '#' or ch == '@':
        co_ky_tu_db = True

do_dai = len(mat_khau)
if (co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_db 
    and do_dai >= 6 and do_dai <= 12):
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")