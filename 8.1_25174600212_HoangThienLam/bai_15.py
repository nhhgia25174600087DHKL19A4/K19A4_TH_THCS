
'''''
ds = [i for i in range(1, 101) if i % 2 == 0]
print(ds)
'''''
from functools import reduce

n = int(input("Nhap n: "))
ds = list(range(1, n+1))

chan = list(filter(lambda x: x % 2 == 0, ds))
tong = reduce(lambda a, b: a + b, chan)

print("Tong chan:", tong)


