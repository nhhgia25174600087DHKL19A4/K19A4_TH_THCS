a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

a0 = a
b0 = b

while b != 0:
    r = a % b
    a = b
    b = r

ucln = a

bcnn = (a0 * b0) // ucln

print("UCLN =", ucln)
print("BCNN =", bcnn)