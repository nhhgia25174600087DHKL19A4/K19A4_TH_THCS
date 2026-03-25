a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
a_goc, b_goc = a, b
dau = 1
if b < 0:
    b = abs(b)
    a = -a
ket_qua = 0
while b > 0:
    if b % 2 != 0:
        ket_qua = ket_qua + a
    a = a + a
    b = b // 2
print(f"Kết quả của {a_goc} x {b_goc} là: {ket_qua}")