m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))
m = abs(m)
n = abs(n)
if m == 0 or n == 0:
    print(f"UCLN là: {m + n}")
else:
    while m != n:
        if m < n:
            m, n = n, m
        r = m - n
        m = r
    print(f"Ước chung lớn nhất là: {m}")
    