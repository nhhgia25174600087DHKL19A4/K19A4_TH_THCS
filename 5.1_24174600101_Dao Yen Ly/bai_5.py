n = int(input("Nhap n: "))

a = []
for i in range(1, n+1):
    a = a + [i]

snt = []
shh = []

for i in a:
    dem = 0
    for j in range(1, i+1):
        if i % j == 0:
            dem = dem + 1
    if dem == 2:
        snt = snt + [i]

    tong = 0
    for j in range(1, i):
        if i % j == 0:
            tong = tong + j
    if tong == i:
        shh = shh + [i]

print("So nguyen to:", snt)
print("So hoan hao:", shh)