def nhap_thong_tin():
    ten = input("Họ tên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))
    return ten, toan, ly, hoa

def tinh_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_thong_tin(ten, toan, ly, hoa):
    dtb = tinh_trung_binh(toan, ly, hoa)
    print(f"Sinh viên: {ten}, ĐTB = {dtb:.2f}")

ten, toan, ly, hoa = nhap_thong_tin()
xuat_thong_tin(ten, toan, ly, hoa)