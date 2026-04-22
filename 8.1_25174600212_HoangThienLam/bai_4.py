def giai_thua(n):
    kq = 1
    for i in range(1, n+1):
        kq *= i
    return kq
n = int(input("Nhap n: "))
print("Giai thua:", giai_thua(n))