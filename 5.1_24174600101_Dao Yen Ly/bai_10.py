n = int(input("Nhap n: "))

# tao tuple ban dau
t = tuple(range(1, n*2))

# loc so le
kq = ()

for i in t:
    if i % 2 != 0:
        kq = kq + (i,)

# lay n phan tu dau
print(kq[:n])