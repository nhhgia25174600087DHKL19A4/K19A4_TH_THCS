import random

def tao_ds(n):
    ds = []
    for i in range(n):
        ds.append(random.randint(1, 100))
    return ds
n = int(input("Nhap n: "))
ds = tao_ds(n)
print("Danh sach:", ds)
kiem_tra_chan = list(map(lambda x: x % 2 == 0, ds))
print("Chan (True/False):", kiem_tra_chan)