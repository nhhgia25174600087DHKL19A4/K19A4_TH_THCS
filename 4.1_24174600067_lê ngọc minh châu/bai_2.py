m = int(input("Nhap m: "))
n = int(input("Nhap n: "))

if m < n:
    temp = m
    m = n
    n = temp
while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m
print("UCLN:", m)