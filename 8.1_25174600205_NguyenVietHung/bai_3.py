#a
def so_nguyen_to():
    n = int(input("Nhập n: "))
    dem = 0

    for i in range(1, n + 1):
        if n % i == 0:
            dem = dem + 1

    if dem == 2:
        print(n, "là số nguyên tố")
    else:
        print(n, "không là số nguyên tố")

#b
def so_hoan_hao():
    n = int(input("Nhập n: "))
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong = tong + i

    if tong == n:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không là số hoàn hảo")

#c
def so_doi_xung():
    dem = 0

    for n in range(1, 1001):
        tam = n
        dao = 0

        while tam > 0:
            du = tam % 10
            dao = dao * 10 + du
            tam = tam // 10

        if dao == n:
            print("%5d" % n, end="")
            dem = dem + 1

            if dem % 15 == 0:
                print()

so_nguyen_to()
so_hoan_hao()
so_doi_xung()