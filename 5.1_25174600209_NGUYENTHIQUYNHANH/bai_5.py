n = int(input("Nhập n: "))
danh_sach_goc = list(range(1, n + 1))
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def la_so_hoan_hao(x):
    if x < 2:
        return False
    tong_uoc = 0
    for i in range(1, x):
        if x % i == 0:
            tong_uoc += i
    return tong_uoc == x
ds_so_nguyen_to = []
ds_so_hoan_hao = []

for so in danh_sach_goc:
    if la_so_nguyen_to(so):
        ds_so_nguyen_to.append(so)
    if la_so_hoan_hao(so):
        ds_so_hoan_hao.append(so)
print(f"Danh sách số nguyên tố từ 1 đến {n}:", ds_so_nguyen_to)
print(f"Danh sách số hoàn hảo từ 1 đến {n}:", ds_so_hoan_hao)
