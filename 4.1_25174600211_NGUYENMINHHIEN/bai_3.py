a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
ket_qua = 0
so_a, so_b = a, b
while b > 0:
    if b % 2 != 0:
        ket_qua = ket_qua + a
    a = a * 2
    b = b // 2
print(f"Kết quả của {so_a} x {so_b} là: {ket_qua}")
