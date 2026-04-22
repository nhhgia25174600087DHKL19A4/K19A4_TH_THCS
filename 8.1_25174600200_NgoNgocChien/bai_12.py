def nhap():
    ho_ten = input("Nhập họ tên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên (năm): "))

    return ho_ten, que_quan, tham_nien
def tinh_luong(tham_nien):
    luong_co_ban = 3000000
    phu_cap = tham_nien * 500000
    return luong_co_ban + phu_cap
def xuat(ho_ten, que_quan, tham_nien, luong):
    print("\n--- THÔNG TIN NHÂN VIÊN ---")
    print("Họ tên:", ho_ten)
    print("Quê quán:", que_quan)
    print("Thâm niên:", tham_nien, "năm")
    print("Lương:", luong, "VND")
ho_ten, que_quan, tham_nien = nhap()
luong = tinh_luong(tham_nien)
xuat(ho_ten, que_quan, tham_nien, luong)