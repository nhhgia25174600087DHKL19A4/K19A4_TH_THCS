import random

def tao_danh_sach(n):
    ds = []
    for i in range(n):
        x = random.randint(1, 100)
        ds.append(x)
    return ds


n = int(input("Nhap n: "))

ds = tao_danh_sach(n)
print("Danh sach vua tao:", ds)

print("Dang kiem tra so chan...")

kq = list(map(lambda x: (x % 2 == 0), ds))

print("Ket qua True/False:", kq)

print("Cac so chan la:")
for i in range(len(ds)):
    if kq[i] == True:
        print(ds[i], end=" ")