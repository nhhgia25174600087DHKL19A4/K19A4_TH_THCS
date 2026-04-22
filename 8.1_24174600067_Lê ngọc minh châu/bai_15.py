#a
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1
    
#b
from functools import reduce
n = int(input("Nhap so luong: "))
ds = []
i = 0
while i < n:
    x = int(input("Nhap so: "))
    ds.append(x)
    i = i + 1
def loc_chan(x):
    return x % 2 == 0
ds_chan = list(filter(loc_chan, ds))
def cong(a, b):
    return a + b
tong = reduce(cong, ds_chan, 0)
print("Tong so chan:", tong)