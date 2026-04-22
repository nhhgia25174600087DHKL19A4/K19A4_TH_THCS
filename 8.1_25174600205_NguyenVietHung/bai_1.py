def tinh_mu():
    so = int(input("Nhập số: "))
    mu = int(input("Nhập số mũ: "))

    t = 1
    dem = 0

    while dem < mu:
        t = t * so
        dem = dem + 1

    print("Kết quả =", t)

tinh_mu()