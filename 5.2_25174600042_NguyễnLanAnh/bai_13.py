ds = input("Nhập các mật khẩu: ").split(",")

ket_qua = []

for mk in ds:
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
        ket_qua.append(mk)

print(",".join(ket_qua))