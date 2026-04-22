import random

def tao_danh_sach(n):
    ds = []
    for i in range(n):
        ds.append(random.randint(1, 100))
    return ds
n = int(input("Nhap n: "))
ds = tao_danh_sach(n)
print("Danh sach:", ds)
binh_phuong = list(map(lambda x: x * x, ds))
print("Binh phuong:", binh_phuong)