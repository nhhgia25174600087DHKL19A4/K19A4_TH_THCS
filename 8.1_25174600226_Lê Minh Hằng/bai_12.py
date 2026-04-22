def nhap():
    ten = input("Tên: ")
    que = input("Quê: ")
    nam = int(input("Số năm làm việc: "))
    return ten, que, nam
def tinh_luong(nam):
    return 3000000 + nam * 500000
def xuat(ten, que, nam, luong):
    print("Tên:", ten)
    print("Quê:", que)
    print("Năm:", nam)
    print("Lương:", luong)
ten, que, nam = nhap()
luong = tinh_luong(nam)
xuat(ten, que, nam, luong)