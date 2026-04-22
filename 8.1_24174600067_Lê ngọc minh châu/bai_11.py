def nhap():
    ten = input("Nhap ten: ")
    toan = float(input("Diem toan: "))
    ly = float(input("Diem ly: "))
    hoa = float(input("Diem hoa: "))
    return ten, toan, ly, hoa

def tinh_tb(t, l, h):
    return (t + l + h) / 3

ten, t, l, h = nhap()
print("Diem trung binh:", tinh_tb(t, l, h))