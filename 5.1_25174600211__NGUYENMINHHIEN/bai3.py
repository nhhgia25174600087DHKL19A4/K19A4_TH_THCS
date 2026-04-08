while True:
    m = int(input("Nhap m: "))
    n = int(input("Nhap n: "))
    if m > 0 and m < n:
        break
    else:
        print("Nhap sai, nhap lai!")
ds = []
for i in range(m, n + 1):
    ds.append(i)
kq = []
for x in ds:
    if x % 2 == 0:
        kq.append(x)
print("Ket qua la:")
print(kq)