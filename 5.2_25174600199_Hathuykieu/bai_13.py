s = input("Nhập các mật khẩu: ")
ds = s.split(',')
ket_qua = []
for mk in ds:
    mk = mk.strip()
    if len(mk) < 6 or len(mk) > 12:
        continue
    co_thuong = co_hoa = co_so = co_dac_biet = False
    for k in mk:
        if k.islower():
            co_thuong = True
        elif k.isupper():
            co_hoa = True
        elif k.isdigit():
            co_so = True
        elif k in "$#@":
            co_dac_biet = True
    if co_thuong and co_hoa and co_so and co_dac_biet:
        ket_qua.append(mk)
print(",".join(ket_qua))