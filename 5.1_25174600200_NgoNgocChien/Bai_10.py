n = int(input("Nhap n: "))
a = []
for i in range(n):
    x = int(input("Nhap so: "))
    a.append(x)
t = tuple(a)
le = []
for i in t:
    if i % 2 != 0:
        le.append(i)
kq = tuple(le)
print("Tuple ban dau:", t)
print("So le:", kq)