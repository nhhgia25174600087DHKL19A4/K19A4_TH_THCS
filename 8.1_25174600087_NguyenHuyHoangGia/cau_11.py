def nhap_thong_tin():
    ten = input("Nhập họ tên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ten, toan, ly, hoa
def tinh_diem_tb(toan, ly, hoa):
    return (toan + ly + hoa) / 3
def xuat_thong_tin(ten, toan, ly, hoa, dtb):
    print("\nBẢNG ĐIỂM SINH VIÊN")
    print(f"Họ và tên: {ten}")
    print(f"Toán: {toan} | Lý: {ly} | Hóa: {hoa}")
    print(f"Điểm trung bình: {dtb:.2f}")
ten_sv, d_toan, d_ly, d_hoa = nhap_thong_tin()
d_tb = tinh_diem_tb(d_toan, d_ly, d_hoa)
xuat_thong_tin(ten_sv, d_toan, d_ly, d_hoa, d_tb)