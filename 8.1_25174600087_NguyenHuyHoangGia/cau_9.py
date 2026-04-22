def phep_tinh_so_hoc():
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    print(f"Cộng: {a} + {b} = {a + b}")
    print(f"Trừ: {a} - {b} = {a - b}")
    print(f"Nhân: {a} * {b} = {a * b}")
    if b != 0:
        print(f"Chia: {a} / {b} = {a / b}")
    else:
        print("Không thể chia")
def tinh_luy_thua():
    x = float(input("Nhập cơ số x: "))
    y = int(input("Nhập số mũ y: "))
    ket_qua = 1
    for _ in range(abs(y)):
        ket_qua *= x
    if y < 0:
        ket_qua = 1 / ket_qua
    print(f"{x} mũ {y} = {ket_qua}")
phep_tinh_so_hoc()
tinh_luy_thua()