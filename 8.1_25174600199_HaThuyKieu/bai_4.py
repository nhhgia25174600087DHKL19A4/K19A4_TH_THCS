n = int(input("Nhập n: "))
#a
def P1(n):
    kq = 1
    for i in range(1, 2 * n + 2, 2):
        kq *= i
    return kq
#b
def S1(n):
    kq = 0
    dau = 1
    for i in range(1, n + 1):
        kq += dau * i
        dau = -dau
    return kq
#c
def S2(n):
    kq = 0
    tam = 0
    for i in range(1, n + 1):
        tam += i
        kq += tam
    return kq
print("P(n) =", P1(n))
print("S(n) câu b =", S1(n))
print("S(n) câu c =", S2(n))
#d
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
n = int(input("Nhập n > 1: "))
def P2(x, y, n):
    kq = x ** y
    for k in range(1, n + 1):
        kq += x + 32 * y + y ** k
    return kq
print("P(x,y) =", P2(x, y, n))