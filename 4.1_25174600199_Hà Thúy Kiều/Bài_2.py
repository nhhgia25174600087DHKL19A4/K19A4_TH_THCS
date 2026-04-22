m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
if m == 0:
    print("UCLN là:", n)
elif n == 0:
    print("UCLN là:", m)
else:
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    print("UCLN là:", m)