def nhap():
    ten = input("Nhập họ tên: ")
    toan = float(input("Toán: "))
    ly = float(input("Lý: "))
    hoa = float(input("Hóa: "))
    return ten, toan, ly, hoa
def tinh_tb(t, l, h):
    return (t + l + h) / 3
def xuat(ten, tb):
    print("Tên:", ten)
    print("Điểm TB:", tb)
ten, t, l, h= nhap()
tb = tinh_tb(t,l,h)
xuat(ten, tb)