# ham ho ten, que và thâm niên
def nhap():
    ten = input("Nhap ho ten: ")
    que = input("Nhap que quan: ")
    nam = int(input("Nhap tham nien (nam): "))
    return ten, que, nam

# ham tinh luong
def tinh_luong(nam):
    luong_co_ban = 3000000
    luong = luong_co_ban + nam * 500000
    return luong

# ham xuat thong tin
def xuat(ten, que, nam, luong):
    print("Ho ten:", ten)
    print("Que quan:", que)
    print("Tham nien:", nam)
    print("Luong:", luong)

#
ten, que, nam = nhap()
luong = tinh_luong(nam)
xuat(ten, que, nam, luong)