n = int(input("Nhap n: "))
a = []
for i in range(1, n+1):
    a = a + [i]
so_nguyen_to = []
so_hoan_hao = []
for i in a:
    dem = 0
    for j in range(1, i+1):
        if i % j == 0:
            dem = dem + 1
    if dem == 2:
        so_nguyen_to = so_nguyen_to + [i]
    tong = 0
    for j in range(1, i):
        if i % j == 0:
            tong = tong + j
    if tong == i:
        so_hoan_hao = so_hoan_hao + [i]
print(so_nguyen_to)
print(so_hoan_hao)