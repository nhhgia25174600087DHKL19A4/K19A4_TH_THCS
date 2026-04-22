import random

def la_nt(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def tao_ds(n):
    ds = []
    i = 0
    while i < n:
        ds.append(random.randint(1, 50))
        i = i + 1
    return ds

n = int(input("Nhap n: "))
ds = tao_ds(n)
print("Danh sach:", ds)
print("So nguyen to:")
i = 0
while i < len(ds):
    if la_nt(ds[i]):
        print(ds[i], end=" ")
    i = i + 1