def nhap():
    ho_ten = input("Nhập họ tên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác: "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    if tham_nien < 1:
        luong = 5000000
    elif tham_nien < 5:
        luong = 7000000
    else:
        luong = 10000000
    return luong

def xuat(ho_ten, que_quan, tham_nien, luong):
    print("Họ tên:", ho_ten)
    print("Quê quán:", que_quan)
    print("Thâm niên công tác:", tham_nien)
    print("Lương:", luong)

ho_ten, que_quan, tham_nien = nhap()
luong = tinh_luong(tham_nien)
xuat(ho_ten, que_quan, tham_nien, luong)