m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
if m < n:
    m, n = n, m

while m != n:
    m = m % n
    if m == 0:
        m = n
        break
    if m < n:
        m, n = n, m

print("ƯCLN là:", m)