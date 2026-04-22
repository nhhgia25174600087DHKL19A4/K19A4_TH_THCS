# thông tin
def nhap():
    ten = input("Nhập họ tên: ")
    que = input("Nhập quê quán: ")
    nam = int(input("Nhập thâm niên công tác (năm): "))
    return ten, que, nam

# lương
def tinh_luong(nam):
    luong_co_ban = 5000000
    phu_cap = nam * 300000
    luong = luong_co_ban + phu_cap
    return luong

# thông tin
def xuat(ten, que, nam, luong):
    print("Họ tên:", ten)
    print("Quê quán:", que)
    print("Thâm niên công tác:", nam, "năm")
    print("Lương:", luong)

# chính
ten, que, nam = nhap()
luong = tinh_luong(nam)
xuat(ten, que, nam, luong)