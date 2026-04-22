def nhap_nhan_vien():
    ten = input("Nhập họ tên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác: "))
    return ten, que_quan, tham_nien
def tinh_luong(tham_nien):
    luong_co_ban = 5000000
    thuong_tham_nien = 500000 * tham_nien
    return luong_co_ban + thuong_tham_nien
def xuat_nhan_vien(ten, que_quan, tham_nien, luong):
    print("\nTHÔNG TIN NHÂN VIÊN")
    print(f"Họ tên: {ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên: {tham_nien} năm")
    print(f"Mức lương: {luong:,.0f} VNĐ")
ten_nv, que_nv, nam_ct = nhap_nhan_vien()
muc_luong = tinh_luong(nam_ct)
xuat_nhan_vien(ten_nv, que_nv, nam_ct, muc_luong)