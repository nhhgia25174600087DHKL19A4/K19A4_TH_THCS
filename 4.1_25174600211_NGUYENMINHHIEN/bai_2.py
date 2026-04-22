m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))
m, n = abs(m), abs(n)
if m == 0 or n == 0:
    print(f"UCLN là: {m + n}")
else:
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    print(f"Ước chung lớn nhất là: {m}")