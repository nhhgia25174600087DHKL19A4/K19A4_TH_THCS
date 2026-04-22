a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

x, y = a, b
while b != 0:
    r = a % b
    a = b
    b = r

UCLN = a
BCNN = (x*y) // UCLN

print("UCLN = ", UCLN)
print("BCNN = ", BCNN)