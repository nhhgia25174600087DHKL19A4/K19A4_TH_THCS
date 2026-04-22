m = int(input("Nhap m: "))
n = int(input("Nhap n: "))

while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m

print("UCLN la:", m)