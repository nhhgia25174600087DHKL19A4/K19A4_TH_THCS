#a
ds_chan = []
for i in range(1, 101):
    if i % 2 == 0:
        ds_chan.append(i)
print("Danh sách số chẵn:", ds_chan)
#b
from functools import reduce
n = int(input("Nhập n: "))
ds = []
for i in range(n):
    x = int(input(f"Nhập số thứ {i+1}: "))
    ds.append(x)
print("Danh sách:", ds)
ds_chan = list(filter(lambda x: x % 2 == 0, ds))
tong = reduce(lambda a, b: a + b, ds_chan, 0)
print("Các số chẵn:", ds_chan)
print("Tổng các số chẵn:", tong)