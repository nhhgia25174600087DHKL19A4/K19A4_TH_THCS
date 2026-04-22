# a)UCLN
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# b)BCNN 
def bcnn(a, b):
    return a * b // ucln(a, b)

# c)
def rut_gon():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))

    g = ucln(tu, mau)

    tu = tu // g
    mau = mau // g

    print("Phân số rút gọn:", tu, "/", mau)

# d)
def lon_nhat_nho_nhat():
    n = int(input("Nhập số lượng số nguyên: "))

    so = int(input("Nhập số thứ 1: "))
    lon = so
    nho = so

    for i in range(2, n + 1):
        so = int(input("Nhập số thứ " + str(i) + ": "))

        if so > lon:
            lon = so

        if so < nho:
            nho = so

    print("Số lớn nhất:", lon)
    print("Số nhỏ nhất:", nho)


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

print("UCLN =", ucln(a, b))
print("BCNN =", bcnn(a, b))

rut_gon()
lon_nhat_nho_nhat()