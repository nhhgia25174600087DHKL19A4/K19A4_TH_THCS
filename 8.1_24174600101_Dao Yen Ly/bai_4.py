# phan a:
def tinh_P(n):
    tich = 1
    i = 0

    while i <= n:
        tich = tich * (2*i + 1)
        i = i + 1

    return tich


n = int(input("Nhap n: "))
print("P(n) =", tinh_P(n))

# phan b:
def tinh_S(n):
    tong = 0
    i = 1

    while i <= n:
        if i % 2 == 0:
            tong = tong - i
        else:
            tong = tong + i
        i = i + 1

    return tong


n = int(input("Nhap n: "))
print("S(n) =", tinh_S(n))

# phan c:
def tinh_S(n):
    tong = 0
    i = 1

    while i <= n:
        j = 1
        tong_con = 0

        while j <= i:
            tong_con = tong_con + j
            j = j + 1

        tong = tong + tong_con
        i = i + 1

    return tong


n = int(input("Nhap n: "))
print("S(n) =", tinh_S(n))

# phan d:
def tinh_P(x, y, n):
    # tinh x^y
    luy_thua = 1
    i = 0
    while i < y:
        luy_thua = luy_thua * x
        i = i + 1

    tong = 0
    k = 1

    while k <= n:
        # tinh y^k
        mu = 1
        j = 0
        while j < k:
            mu = mu * y
            j = j + 1

        tong = tong + (x + 32*y + mu)
        k = k + 1

    return luy_thua + tong


x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
n = int(input("Nhap n (>1): "))

print("P(x, y) =", tinh_P(x, y, n))
