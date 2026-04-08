while True:
    m = int(input("Nhap m: "))
    n = int(input("Nhap n: "))
    if m > 0 and m < n:
        break

a = []
for i in range(m, n+1):
    a = a + [i]

b = []
for i in a:
    if i % 2 == 0:
        b = b + [i]

print(b)
