password = input("Nhập mật khẩu: ")

ok = True

if not (6 <= len(password) <= 12):
    ok = False

co_thuong = co_hoa = co_so = co_ky_tu = False

for c in password:
    if 'a' <= c <= 'z': co_thuong = True
    elif 'A' <= c <= 'Z': co_hoa = True
    elif '0' <= c <= '9': co_so = True
    elif c in "$#@": co_ky_tu = True

if not (co_thuong and co_hoa and co_so and co_ky_tu):
    ok = False

print("Hợp lệ" if ok else "Không hợp lệ")