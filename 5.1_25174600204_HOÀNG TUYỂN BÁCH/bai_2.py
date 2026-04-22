n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
a = []
for i in range(1, n + 1):
    a.append(i * i)
if m >= n:
    print([])
else:
    for i in range(m, n):
        print(a[i], end=" ")