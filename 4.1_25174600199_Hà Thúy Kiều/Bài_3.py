a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
ket_qua = 0
dau = 1
if b < 0:
    b = -b
    dau = -1
while b > 0:
    if b % 2 == 1:
        ket_qua += a
    a *= 2
    b //= 2
print("Kết quả:", ket_qua * dau)