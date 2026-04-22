#a:
a = []
for i in range(1, 101):
    if i % 2 == 0:
       a.append(i)
print("Danh sách số chẵn:", a)

#b:
from functools import reduce
n = int(input("Nhập số lượng phần tử: "))
m = []
for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    m.append(x)
s= list(filter(lambda x: x % 2 == 0, m))
tong = reduce(lambda a, b: a + b, s, 0)
print("Danh sách ban đầu:", m)
print("Số chẵn:", s)
print("Tổng số chẵn:", tong)