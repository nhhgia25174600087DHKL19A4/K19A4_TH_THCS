m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m
print("UCLN là:", m) 