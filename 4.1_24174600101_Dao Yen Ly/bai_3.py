def nhan_an_do(a, b):
    ket_qua = 0
    while b > 0:
        if b % 2 == 1:
            ket_qua += a
        a *= 2
        b //= 2
    return ket_qua

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

print("Ket qua:", nhan_an_do(a, b))