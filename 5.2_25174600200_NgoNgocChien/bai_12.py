username = input("Nhập username: ")
password = input("Nhập password: ")
co_chu_thuong = False
co_chu_hoa = False
co_so = False
co_ky_tu_db = False
if len(password) >= 6 and len(password) <= 12:
    for i in password:
        if i >= 'a' and i <= 'z':
            co_chu_thuong = True
        elif i >= 'A' and i <= 'Z':
            co_chu_hoa = True
        elif i >= '0' and i <= '9':
            co_so = True
        elif i == '$' or i == '#' or i == '@':
            co_ky_tu_db = True
    if co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_db:
        print("Mật khẩu hợp lệ")
    else:
        print("Mật khẩu không hợp lệ")
else:
    print("Độ dài mật khẩu không hợp lệ")