def nhap():
    ten = input("Ten: ")
    toan = float(input("Toan: "))
    ly = float(input("Ly: "))
    hoa = float(input("Hoa: "))
    return ten, toan, ly, hoa
def tb(t, l, h):
    return (t + l + h) / 3
def xuat(ten, dtb):
    print("Ten:", ten)
    print("DTB:", dtb)
ten, t, l, h = nhap()
dtb = tb(t, l, h)
xuat(ten, dtb)