def tinh_luy_thua():
    a = int(input("Nhập cơ số (a): "))
    n = int(input("Nhập số mũ (n): "))
    ket_qua = 1
    for _ in range(n):
        ket_qua *= a
    print(f"{a}^{n} = {ket_qua}")

tinh_luy_thua()