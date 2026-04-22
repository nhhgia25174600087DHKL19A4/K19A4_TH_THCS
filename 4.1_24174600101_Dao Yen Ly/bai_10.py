# phan a
n = int(input("Nhap n: "))

for i in range(2, n+1):
    la_snt = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            la_snt = False
            break
    if la_snt:
        print(i, end=" ")

# phan b
n = int(input("Nhap n: "))

for i in range(1, n+1):
    tong = 0
    for j in range(1, i):
        if i % j == 0:
            tong += j
    if tong == i:
        print(i, end=" ")
