#a:
def ucln(a, b):
    while b != 0:
        a = a % b
        a, b = b, a
    return a
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN là:", ucln(a, b))

#b:
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return (a * b) // ucln(a, b)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("BCNN là:", bcnn(a, b))

#c:
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def rut_gon():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    u = ucln(tu, mau)
    tu //= u
    mau //= u
    print("Phân số rút gọn:", tu, "/", mau)
rut_gon()

#d:
def tim_min_max():
    n = int(input("Nhập số lượng phần tử: "))
    x = int(input("Nhập số thứ 1: "))
    min_val = x
    max_val = x
    for i in range(2, n + 1):
        x = int(input(f"Nhập số thứ {i}: "))
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    print("Số nhỏ nhất:", min_val)
    print("Số lớn nhất:", max_val)
tim_min_max()