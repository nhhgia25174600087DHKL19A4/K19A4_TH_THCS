def check_password(pw):
    if len(pw) < 6 or len(pw) > 12:
        return False

    co_thuong = False
    co_hoa = False
    co_so = False
    co_dac_biet = False

    for c in pw:
        if 'a' <= c <= 'z':
            co_thuong = True
        elif 'A' <= c <= 'Z':
            co_hoa = True
        elif '0' <= c <= '9':
            co_so = True
        elif c in "$#@":
            co_dac_biet = True

    return co_thuong and co_hoa and co_so and co_dac_biet


# nhập nhiều mật khẩu
s = input("Nhập các mật khẩu (cách nhau dấu phẩy): ")
ds = s.split(",")

ket_qua = []

for pw in ds:
    pw = pw.strip()   # bỏ khoảng trắng
    if check_password(pw):
        ket_qua.append(pw)

print(",".join(ket_qua))