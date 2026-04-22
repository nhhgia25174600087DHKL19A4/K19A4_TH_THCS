n = int(input("Nhập n: "))
day_so  = list(range(1, n + 1))

so_nguyen_to = []
for x in day_so:
    if x > 1:
        la_so_nt = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                la_so_nt = False
                break
        if la_so_nt:
            so_nguyen_to.append(x)

so_hoan_hao = []
for x in day_so:
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong = tong + i
    if tong == x:
        so_hoan_hao.append(x)

ket_qua = (so_nguyen_to, so_hoan_hao)
print("Số nguyên tố là: ", ket_qua[0])
print("Số hoàn hảo: ", ket_qua[1])