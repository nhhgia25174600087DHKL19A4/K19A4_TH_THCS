# Hàm tính 4 phép toán
def tinh_toan(a, b):
    print("Cộng:", a + b)
    print("Trừ:", a - b)
    print("Nhân:", a * b)
    if b != 0:
        print("Chia:", a / b)
    else:
        print("Không chia được cho 0")

# Hàm tính lũy thừa
def luy_thua():
    a = int(input("Nhập a: "))
    n = int(input("Nhập n: "))
    kq = 1
    for i in range(n):
        kq = kq * a
    print("Lũy thừa:", kq)

# Chương trình chính 
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
tinh_toan(a, b)
luy_thua()