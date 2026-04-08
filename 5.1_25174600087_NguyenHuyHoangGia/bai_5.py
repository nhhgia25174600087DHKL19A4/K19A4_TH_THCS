n = int(input("Nhap n: "))
ds_goc = []
for i in range(1, n + 1):
    ds_goc.append(i)
ds_nguyen_to = []
ds_hoan_hao = []
for so in ds_goc:
    dem_uoc = 0
    for i in range(1, so + 1):
        if so % i == 0:
            dem_uoc += 1
    if dem_uoc == 2:
        ds_nguyen_to.append(so)
    tong_uoc = 0
    for j in range(1, so):
        if so % j == 0:
            tong_uoc += j
    if tong_uoc == so and so != 0:
        ds_hoan_hao.append(so)
print("Cac so nguyen to tim thay:", ds_nguyen_to)
print("Cac so hoan hao tim thay:", ds_hoan_hao)