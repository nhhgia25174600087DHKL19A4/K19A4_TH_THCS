def phep_toan(a, b):
    print("Cộng:", a + b)
    print("Trừ:", a - b)
    print("Nhân:", a * b)
    if b != 0:
        print("Chia:", a / b)
    else:
        print("Không thể chia cho 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
phep_toan(a, b)  
#phần luỹ thừa
def luy_thua(a, b, n):
    kq1 = a ** (b + n)
    kq2 = (b ** (n + 2)) * a
    print("a^(b+n) =", kq1)
    print("b^(n+2) * a =", kq2)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
n = int(input("Nhập n: "))
luy_thua(a, b, n)