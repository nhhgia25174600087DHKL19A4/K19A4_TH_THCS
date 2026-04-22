def nhap_thong_tin():
    ho_ten = input("Nhập họ tên sinh viên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly   = float(input("Nhập điểm Lý: "))
    hoa  = float(input("Nhập điểm Hóa: "))
    return ho_ten, toan, ly, hoa

def xuat_thong_tin(ho_ten, toan, ly, hoa, tb):
    print("\n--- Thông tin sinh viên ---")
    print(f"Họ tên: {ho_ten}")
    print(f"Điểm Toán: {toan}")
    print(f"Điểm Lý: {ly}")
    print(f"Điểm Hóa: {hoa}")
    print(f"Điểm trung bình: {tb:.2f}")

# tính điểm trung bình
def tinh_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def main():
    ho_ten, toan, ly, hoa = nhap_thong_tin()
    tb = tinh_trung_binh(toan, ly, hoa)
    xuat_thong_tin(ho_ten, toan, ly, hoa, tb)

main()
