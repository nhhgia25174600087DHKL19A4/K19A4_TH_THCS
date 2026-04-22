# a)
def cau_a():
    n = int(input("Nhập n: "))
    tich = 1

    for i in range(n + 1):
        tich = tich * (2 * i + 1)

    print("P(n) =", tich)

# b)
def cau_b():
    n = int(input("Nhập n: "))
    tong = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            tong = tong - i
        else:
            tong = tong + i

    print("S(n) =", tong)

# c)
def cau_c():
    n = int(input("Nhập n: "))
    tong = 0

    for i in range(1, n + 1):
        phu = 0
        for j in range(1, i + 1):
            phu = phu + j
        tong = tong + phu

    print("S(n) =", tong)

# d)
def cau_d():
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    n = int(input("Nhập n: "))

    mu = 1
    for i in range(y):
        mu = mu * x

    tong = 0
    for k in range(1, n + 1):
        yk = 1
        for i in range(k):
            yk = yk * y

        tong = tong + (x + 32 * y + yk)

    kq = mu + tong

    print("P(x,y) =", kq)

cau_a()
cau_b()
cau_c()
cau_d()