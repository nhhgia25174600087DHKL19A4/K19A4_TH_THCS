n = int(input("Nhap n: "))
m = int(input("Nhap m: "))

a = []
for i in range(1, n+1):
    a = a + [i*i]

if m >= n:
    print([])
else:
    print(a[m:])