#a
def uoc_chung_lon_nhat(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#b
def boi_chung_nho_nhat(a, b):
    return a * b // uoc_chung_lon_nhat(a, b)
#c
tu = int(input("Nhap tu: "))
mau = int(input("Nhap mau: "))
g = uoc_chung_lon_nhat(tu, mau)
print("Phan so rut gon:", tu//g, "/", mau//g)

#d
n = int(input("Nhap so luong: "))
i = 0
while i < n:
    x = input("Nhap so: ")
    if x == "":
        print("Ban chua nhap, nhap lai!")
        continue
    a = int(x)
    if i == 0:
        lon = a
        nho = a
    else:
        if a > lon:
            lon = a
        if a < nho:
            nho = a
    i = i + 1
print("So lon nhat:", lon)
print("So nho nhat:", nho)