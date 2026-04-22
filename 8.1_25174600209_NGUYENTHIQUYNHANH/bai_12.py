def nhap_nhan_vien():
    ho_ten = input("Nhập họ tên nhân viên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (số năm): "))
    return ho_ten, que_quan, tham_nien
def tinh_luong(tham_nien):
    luong_co_ban = 5000000 
    phu_cap_tham_nien = tham_nien * 500000
    tong_luong = luong_co_ban + phu_cap_tham_nien
    return tong_luong
def xuat_nhan_vien(ten, que, tn, luong):
    print("\n--- Thông tin nhân viên ---")
    print("Họ tên: {}".format(ten))
    print("Quê quán: {}".format(que))
    print("Thâm niên: {} năm".format(tn))
    print("Tổng lương: {:,} VNĐ".format(luong))
def bai_12():
    ten, que, tn = nhap_nhan_vien()
    luong = tinh_luong(tn)
    xuat_nhan_vien(ten, que, tn, luong)
bai_12()