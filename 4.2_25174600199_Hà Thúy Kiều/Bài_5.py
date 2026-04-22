a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
x, y = a, b
for _ in range(1000000):
    if b == 0:
        break
    a, b = b, a % b
ucln = a
bcnn = abs(x*y) // ucln
print("UCLN =", ucln)
print("BCNN =", bcnn)