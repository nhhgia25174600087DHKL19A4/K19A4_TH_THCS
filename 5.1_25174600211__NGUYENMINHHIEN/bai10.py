n = int(input("Nhap so luong phan tu n: "))
L = []
for i in range(n):
    so = int(input(f"Nhap phan tu thu {i+1}: "))
    L.append(so)
tup_goc = tuple(L)
print("Tuple ban dau:", tup_goc)
kq = []
for x in tup_goc:
    if x > 0 and x % 2 != 0:
        kq.append(x)
tup_le = tuple(kq)
print("Tuple cac so duong le la:", tup_le)
