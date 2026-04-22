def nhap():
    ten = input("Ten: ")
    que = input("Que: ")
    nam = int(input("Tham nien: "))
    return ten, que, nam


def tinh_luong(nam):
    luong = nam * 1000
    return luong


def xuat(ten, que, nam, luong):
    print("Ten:", ten)
    print("Que:", que)
    print("Nam:", nam)
    print("Luong:", luong)


ten, que, nam = nhap()
luong = tinh_luong(nam)
xuat(ten, que, nam, luong)