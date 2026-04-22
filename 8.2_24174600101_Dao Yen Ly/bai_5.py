import random

def la_nguyen_to(n):
    if n < 2:
        return False

    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1

    return True

def tao_danh_sach(n):
    ds = [0] * n
    i = 0
    while i < n:
        ds[i] = int(random.random() * 100) + 1
        i = i + 1
    return ds

n = int(input("Nhap n: "))

ds = tao_danh_sach(n)
print("Danh sach:", ds)

print("So nguyen to:")
for i in range(n):
    if la_nguyen_to(ds[i]):
        print(ds[i], end=" ")