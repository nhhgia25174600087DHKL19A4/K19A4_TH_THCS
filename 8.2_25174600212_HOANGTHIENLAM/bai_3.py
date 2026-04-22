import random

def la_snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def tao_ds(n):
    ds = []
    for i in range(n):
        ds.append(random.randint(1, 100))
    return ds
n = int(input("Nhap n: "))
ds = tao_ds(n)
print("Danh sach:", ds)

print("So nguyen to:")
for x in ds:
    if la_snt(x):
        print(x, end=" ")