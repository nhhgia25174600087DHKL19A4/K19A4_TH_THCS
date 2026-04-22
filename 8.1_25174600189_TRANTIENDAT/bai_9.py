def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Không chia được cho 0"
    return a / b

def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Không chia được cho 0"
    return a / b

def main():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))

    print("Cộng:", cong(a, b))
    print("Trừ:", tru(a, b))
    print("Nhân:", nhan(a, b))
    print("Chia:", chia(a, b))

    n = int(input("Nhập số mũ n (>=0): "))
    print("Lũy thừa a^n =", luy_thua(a, n))

main()