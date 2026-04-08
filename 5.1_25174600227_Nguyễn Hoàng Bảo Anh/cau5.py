n = int(input("Nhập n: "))
ds_goc = list(range(1, n + 1))

ds_nguyento = []
ds_hoanhao = []

for x in ds_goc:
  
    if x > 1:
        check_nguyento = True
        for i in range(2, x):
            if x % i == 0:
                check_nguyento = False
                break
        if check_nguyento:
            ds_nguyento = ds_nguyento + [x]

    tong_uoc = 0
    for j in range(1, x):
        if x % j == 0:
            tong_uoc = tong_uoc + j
    if tong_uoc == x and x != 0:
        ds_hoanhao = ds_hoanhao + [x]

print("Số nguyên tố:", ds_nguyento)
print("Số hoàn hảo:", ds_hoanhao)