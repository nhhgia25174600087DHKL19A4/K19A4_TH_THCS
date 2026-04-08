mk = input("Nhập mật khẩu: ")

co_thuong = False
co_hoa = False
co_so = False
co_ky_tu = False

for c in mk:
    if 'a' <= c <= 'z':
        co_thuong = True
    elif 'A' <= c <= 'Z':
        co_hoa = True
    elif '0' <= c <= '9':
        co_so = True
    elif c == '$' or c == '#' or c == '@':
        co_ky_tu = True

if co_thuong and co_hoa and co_so and co_ky_tu and len(mk) >= 6:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")