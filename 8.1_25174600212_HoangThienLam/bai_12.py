def nhap():
    ten = input("Nhap ho ten: ")
    que = input("Nhap que quan: ")
    nam = int(input("Nhap tham nien (so nam): "))
    return ten, que, nam
def tinh_luong(nam):
    luong = 3000000 + nam * 500000
    return luong
def xuat(ten, que, nam, luong):
    print("Ho ten:", ten)
    print("Que quan:", que)
    print("Tham nien:", nam)
    print("Luong:", luong)
ten, que, nam = nhap()
luong = tinh_luong(nam)
xuat(ten, que, nam, luong)