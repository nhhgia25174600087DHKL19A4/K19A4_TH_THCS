def P(n):
    tich = 1
    for i in range(n + 1):
        tich *= (2 * i + 1)
    return tich

def S1(n):
    tong = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            tong += i
        else:
            tong -= i
    return tong

def S2(n):
    tong = 0
    tam = 0
    for i in range(1, n + 1):
        tam += i
        tong += tam
    return tong

def Pxy(x, y, n):
    tong = x ** y
    for k in range(1, n + 1):
        tong += (x + 9 * y + y ** k)
    return tong

n = int(input("Nhập n: "))
print("P(n) =", P(n))
print("S1(n) =", S1(n))
print("S2(n) =", S2(n))

x = float(input("Nhập x: "))
y = float(input("Nhập y: "))
print("P(x, y) =", Pxy(x, y, n))