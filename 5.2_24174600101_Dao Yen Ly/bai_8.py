n = int(input("nhap n: "))

a = []

# gan 2 so dau
a.append(0)
a.append(1)

# tao tiep
for i in range(2, n):
    x = a[i-1] + a[i-2]
    a.append(x)

# in ra
for i in range(n):
    print(a[i], end=" ")
    