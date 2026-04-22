#a
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print("UCLN =", ucln(a, b))

#b
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return a * b // ucln(a, b)
print("BCNN =", bcnn(a, b))

#c
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def rut_gon(tu, mau):
    g = ucln(tu, mau)
    return tu // g, mau // g
tu, mau = rut_gon(tu, mau)
print("Phân số rút gọn:", tu, "/", mau)

#d
n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Phần tử {i+1}: ")))
mn = mx = arr[0]
for x in arr:
    if x < mn:
        mn = x
    if x > mx:
        mx = x
print("Nhỏ nhất:", mn)
print("Lớn nhất:", mx)