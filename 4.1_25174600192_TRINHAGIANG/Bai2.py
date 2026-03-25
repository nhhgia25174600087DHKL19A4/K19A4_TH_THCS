m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))

if m < n:
    m, n = n, m

while m != n:
    r = m - n
    if r > n:
        m = r
    else:
        m, n = n, r

print("UCLN là:", m)