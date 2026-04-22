n = int(input("Nhap n: "))
t = tuple(range(1, n*2))
kq = ()
for i in t:
    if i % 2 != 0:
        kq = kq + (i,)
print(kq[:n])