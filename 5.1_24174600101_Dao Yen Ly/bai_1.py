n = int(input("Nhap n: "))
m = int(input("Nhap m: "))

a = []

for i in range(1, n+1):
    a.append(i*i)

if m >= n:
    print(a)
else:
    print(a[0:m])
    