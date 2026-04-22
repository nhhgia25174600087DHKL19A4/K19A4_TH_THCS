s = input("Nhập các mật khẩu (cách nhau bởi dấu phẩy): ")
passwords = [p.strip() for p in s.split(",")]
valid = []
for password in passwords:
    co_chu_thuong = False
    co_chu_hoa = False
    co_so = False
    co_ky_tu_db = False

    for c in password:
        if 'a' <= c <= 'z':
            co_chu_thuong = True
        elif 'A' <= c <= 'Z':
            co_chu_hoa = True
        elif '0' <= c <= '9':
            co_so = True
        elif c in ['$', '#', '@']:
            co_ky_tu_db = True

    if (co_chu_thuong and co_chu_hoa and co_so and co_ky_tu_db and 6 <= len(password) <= 12):
        valid.append(password)

result = ""
for i in range(len(valid)):
    result += valid[i]
    if i != len(valid) - 1:
        result += ","

print(result)