def nhap():
    ten = input("Nhập họ tên: ")
    que = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên (năm): "))
    return ten, que, tham_nien

# Hàm tính lương
def tinh_luong(tham_nien):
    luong_cb = 1500000
    luong = luong_cb + tham_nien * 200000
    return luong

# Hàm xuất
def xuat(ten, que, tham_nien, luong):
    print("Họ tên:", ten)
    print("Quê quán:", que)
    print("Thâm niên:", tham_nien, "năm")
    print("Lương:", luong)

# Chương trình chính 
ten, que, tham_nien = nhap()
luong = tinh_luong(tham_nien)
xuat(ten, que, tham_nien, luong)