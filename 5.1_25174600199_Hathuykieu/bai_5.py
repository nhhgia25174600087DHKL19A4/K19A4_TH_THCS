n = int(input("Nhập n: "))
ds_nguyen_to = []
ds_hoan_hao = []
for x in range(1, n + 1):
    if x >= 2:
        la_nguyen_to = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            ds_nguyen_to.append(x)
    if x > 1:
        tong_uoc = 0
        for i in range(1, x):
            if x % i == 0:
                tong_uoc += i
        if tong_uoc == x:
            ds_hoan_hao.append(x)
print("Danh sách số nguyên tố:", ds_nguyen_to)
print("Danh sách số hoàn hảo:", ds_hoan_hao)