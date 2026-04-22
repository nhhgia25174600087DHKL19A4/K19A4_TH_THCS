import random
def tao_ds(n):
    ds = []
    i = 0
    while i < n:
        ds.append(random.randint(1, 10))
        i = i + 1
    binh_phuong = list(map(lambda x: x*x, ds))
    return ds, binh_phuong

n = int(input("Nhap n: "))
ds, kq = tao_ds(n)

print("Danh sach:", ds)
print("Binh phuong:", kq)