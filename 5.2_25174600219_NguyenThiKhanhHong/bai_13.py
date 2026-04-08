n = input("Nhập các mật khẩu cách nhau bởi dấu phẩy: ")
danh_sach_cho = n.split(',')
ket_qua_cuoi = []
for mk in danh_sach_cho:
    mk = mk.strip() 
    check_a = any('a' <= c <= 'z' for c in mk)
    check_b = any('0' <= c <= '9' for c in mk)
    check_c = any('A' <= c <= 'Z' for c in mk)
    check_d = any(c in "$#@ " for c in mk)
    check_ef = 6 <= len(mk) <= 12
    if check_a and check_b and check_c and check_d and check_ef:
        ket_qua_cuoi.append(mk)
print(",".join(ket_qua_cuoi))