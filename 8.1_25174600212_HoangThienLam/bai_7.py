#a
'''''
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print("UCLN:", ucln(a, b))
'''''
'''''
#b,
def bcnn(a, b):
    return a * b // ucln(a, b)

print("BCNN:", bcnn(a, b))
'''''
'''''
tu = int(input("Nhap tu: "))
mau = int(input("Nhap mau: "))

u = ucln(tu, mau)

print("Rut gon:", tu//u, "/", mau//u)
'''''
n = int(input("Nhap so luong: "))
ds = []

for i in range(n):
    x = int(input("Nhap so: "))
    ds.append(x)

print("Max:", max(ds))
print("Min:", min(ds))