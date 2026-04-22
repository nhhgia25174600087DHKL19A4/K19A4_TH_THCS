n = int(input("Nhap n: "))

ds = []
for i in range(1, n+1):
    ds.append(i)
nt = []

for x in ds:
    if x < 2:
        continue
    dem = 0
    for i in range(1, x+1):
        if x % i == 0:
            dem += 1
    if dem == 2:
        nt.append(x)
hh = []
for x in ds:
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    if tong == x:
        hh.append(x)
print("So nguyen to:", nt)
print("So hoan hao:", hh)