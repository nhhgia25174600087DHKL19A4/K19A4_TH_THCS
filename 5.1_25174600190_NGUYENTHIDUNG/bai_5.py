n = int(input("Nhập n: "))
dãy_so = list(range(1, n + 1))

ds_nguyen_to = []
for so in dãy_so:
    if so > 1:
        la_nguyen_to = True
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            ds_nguyen_to.append(so)

ds_hoan_hao = []
for so in dãy_so:
    tong_uoc = 0
    for i in range(1, so):
        if so % i == 0:
            tong_uoc += i
    if tong_uoc == so and so != 0:
        ds_hoan_hao.append(so)

print("Số nguyên tố:", ds_nguyen_to)
print("Số hoàn hảo:", ds_hoan_hao)