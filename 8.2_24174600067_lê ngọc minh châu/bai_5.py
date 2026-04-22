import random
def tao_ds(n):
    ds = []
    i = 0
    while i < n:
        ds.append(random.randint(1, 20))
        i = i + 1
    kq = list(map(lambda x: True if x % 2 == 0 else False, ds))
    
    return ds, kq

n = int(input("Nhap n: "))
ds, kq = tao_ds(n)
print("Danh sach:", ds)
print("Chan hay khong:", kq)