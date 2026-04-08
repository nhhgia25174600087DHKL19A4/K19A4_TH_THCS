n = int(input("Nhap n: "))
m = int(input("Nhap m: "))
ds = []
for i in range(1, n + 1):
    ds.append(i * i)
if m >= n:
    print("Ket qua la:")
    print(ds)
else:
    kq = []
    i = 0
    while i < m:
        kq.append(ds[i])
        i = i + 1
    print("Ket qua la:")
    print(kq)