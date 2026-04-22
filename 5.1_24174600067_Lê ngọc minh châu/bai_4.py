while True:
    m = int(input("Nhap m: "))
    n = int(input("Nhap n: "))
    if m > 0 and m < n:
        break
a = []
i = m
while i <= n:
    a = a + [i]
    i = i + 2
a = a[0:100]
tong = 0
for i in a:
    tong = tong + i
print(a)
print("Tong =", tong)