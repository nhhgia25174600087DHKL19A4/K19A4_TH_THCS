def nhap():
    ten = input("Nhap ten: ")
    toan = float(input("Toan: "))
    ly = float(input("Ly: "))
    hoa = float(input("Hoa: "))
    return ten, toan, ly, hoa


def tinh_tb(t, l, h):
    return (t + l + h) / 3


def xuat(ten, tb):
    print("Ten:", ten)
    print("Diem TB:", tb)


ten, t, l, h = nhap()
tb = tinh_tb(t, l, h)
xuat(ten, tb)