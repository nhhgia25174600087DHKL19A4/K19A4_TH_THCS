# Hàm cộng
def cong(a, b):
    return a + b

# Hàm trừ
def tru(a, b):
    return a - b

# Hàm nhân
def nhan(a, b):
    return a * b

# Hàm chia
def chia(a, b):
    if b != 0:
        return a / b
    else:
        return "Không chia được"

# Hàm lũy thừa a^n
def luy_thua(a, n):
    kq = 1
    for i in range(n):
        kq = kq * a
    return kq


a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

print("Tổng =", cong(a, b))
print("Hiệu =", tru(a, b))
print("Tích =", nhan(a, b))
print("Thương =", chia(a, b))

n = int(input("Nhập số mũ n: "))
print("Lũy thừa =", luy_thua(a, n))