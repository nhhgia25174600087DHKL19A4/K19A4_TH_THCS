# a)
def ucln(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN =", ucln(a, b))

# b)
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return (a * b) // ucln(a, b)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("BCNN =", bcnn(a, b))

# c)
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon(tu, mau):
    u = ucln(tu, mau)
    tu = tu // u
    mau = mau // u
    return tu, mau

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

tu, mau = rut_gon(tu, mau)
print("Phân số rút gọn:", tu, "/", mau)

# d)
def tim_min_max(n):
    x = int(input("Nhập số thứ 1: "))
    min_val = x
    max_val = x

    for i in range(2, n + 1):
        x = int(input(f"Nhập số thứ {i}: "))

        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    return min_val, max_val


n = int(input("Nhập n: "))
mn, mx = tim_min_max(n)

print("Min =", mn)
print("Max =", mx)