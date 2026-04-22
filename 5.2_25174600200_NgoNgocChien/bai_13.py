s = input("Nhập các mật khẩu: ")
ds = s.split(",")
ketqua = []
for password in ds:
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
            ketqua.append(password)
print(",".join(ketqua))