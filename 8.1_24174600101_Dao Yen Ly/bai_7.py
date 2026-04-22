# phan a:
def ucln(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print("UCLN =", ucln(a, b))

# phan b:
def ucln(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def bcnn(a, b):
    return a * b // ucln(a, b)


a = int(input())
b = int(input())
print("BCNN =", bcnn(a, b))

# phan c:
def ucln(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


tu = int(input("Nhap tu: "))
mau = int(input("Nhap mau: "))

g = ucln(tu, mau)

print("Phan so rut gon:", tu // g, "/", mau // g)

# phan d:
n = int(input("Nhap n: "))
ds = []
for i in range(n):
    ds.append(int(input()))

print("Max:", max(ds))
print("Min:", min(ds))