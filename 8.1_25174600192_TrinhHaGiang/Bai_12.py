def nhap_thong_tin():
    ho_ten = input("Nhập họ tên nhân viên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (năm): "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    luong_co_ban = 5000000
    phu_cap = 500000 * tham_nien
    return luong_co_ban + phu_cap

def xuat_thong_tin(ho_ten, que_quan, tham_nien, luong):
    print("\n--- Thông tin nhân viên ---")
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên công tác: {tham_nien} năm")
    print(f"Lương: {luong:,} VNĐ")

def main():
    ho_ten, que_quan, tham_nien = nhap_thong_tin()
    luong = tinh_luong(tham_nien)
    xuat_thong_tin(ho_ten, que_quan, tham_nien, luong)
main()
