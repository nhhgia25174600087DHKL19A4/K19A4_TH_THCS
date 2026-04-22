# a
def cau_a(n):
    p = 1
    i = 0
    while i <= n:
        p = p * (2*i + 1)
        i = i + 1
    return p

# b
def cau_b(n):
    s = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            s = s - i
        else:
            s = s + i
        i = i + 1
    return s

# c
def cau_c(n):
    s = 0
    i = 1
    tong_phu = 0
    while i <= n:
        tong_phu = tong_phu + i
        s = s + tong_phu
        i = i + 1
    return s

# d
def luy_thua(a, b):
    kq = 1
    i = 0
    while i < b:
        kq = kq * a
        i = i + 1
    return kq
def cau_d(x, y, n):
    tong = 0
    k = 1
    while k <= n:
        tong = tong + (x + luy_thua(3, y) + luy_thua(y, k))
        k = k + 1
    return luy_thua(x, y) + tong

n = int(input("Nhap n: "))
print("Cau a:", cau_a(n))
print("Cau b:", cau_b(n))
print("Cau c:", cau_c(n))
x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
n2 = int(input("Nhap n (cho cau d): "))
print("Cau d:", cau_d(x, y, n2))