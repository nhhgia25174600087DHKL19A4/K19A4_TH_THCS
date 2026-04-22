m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
m = abs(m)
n = abs(n)
ucln = 1
min_val = m if m < n else n
for i in range(min_val, 0, -1):
    if m % i == 0 and n % i == 0:
        ucln = i
        break
print("UCLN là:", ucln)