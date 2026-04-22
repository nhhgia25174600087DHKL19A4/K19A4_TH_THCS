n = int(input("Nhap n: "))
m = int(input("Nhap m: "))
a = []
i = 1
while i <= n:
    a = a + [i*i]
    i = i + 1
if m >= n:
    print(a)
else:
    print(a[0:m])