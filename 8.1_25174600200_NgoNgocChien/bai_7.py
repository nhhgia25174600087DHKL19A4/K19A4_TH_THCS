#a
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN =", ucln(a, b))
#b
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("BCNN =", bcnn(a, b))
#c
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def rut_gon(tu, mau):
    u = ucln(tu, mau)
    tu //= u
    mau //= u
    return tu, mau

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
tu, mau = rut_gon(tu, mau)
print("Phân số rút gọn:", tu, "/", mau)
#d
n = int(input("Nhập số lượng phần tử n: "))
ds = []
for i in range(n):
    x = int(input(f"Nhập số thứ {i+1}: "))
    ds.append(x)
min_val = ds[0]
max_val = ds[0]
for x in ds:
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x
print("Số nhỏ nhất:", min_val)
print("Số lớn nhất:", max_val)