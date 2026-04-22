def luy_thua():
    a = int(input("Nhap a: "))
    n = int(input("Nhap n: "))
    kq = 1
    for i in range(n):
        kq *= a
    print("Ket qua:", kq)

luy_thua()