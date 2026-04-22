def tinh_luy_thua():
    a = int(input("Nhap a: "))
    n = int(input("Nhap n: "))
    kq = 1
    i = 0
    while i < n:
        kq = kq * a
        i = i + 1
    print("Ket qua:", kq)
tinh_luy_thua()