def nhap():
    ten = input("Họ tên: ")
    que = input("Quê quán: ")
    nam = int(input("Thâm niên (năm): "))
    return ten, que, nam
def tinh_luong(nam):
    if nam < 5:
        return 5000000
    elif nam <= 10:
        return 8000000
    else:
        return 12000000
def xuat(ten, que, nam, luong):
    print("Họ tên:", ten)
    print("Quê:", que)
    print("Thâm niên:", nam)
    print("Lương:", luong)
ten, que, nam = nhap()
luong = tinh_luong(nam)
xuat(ten, que, nam, luong)