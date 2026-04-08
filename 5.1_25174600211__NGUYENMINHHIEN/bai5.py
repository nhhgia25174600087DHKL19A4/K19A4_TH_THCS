n = int(input("Nhập n: "))
ds = list(range(1, n + 1))
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def la_so_hoan_hao(x):
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    return tong == x
ds_nguyen_to = []
ds_hoan_hao = []
for i in ds:
    if la_so_nguyen_to(i):
        ds_nguyen_to.append(i)
    if la_so_hoan_hao(i):
        ds_hoan_hao.append(i)
print("Số nguyên tố:", ds_nguyen_to)
print("Số hoàn hảo:", ds_hoan_hao)