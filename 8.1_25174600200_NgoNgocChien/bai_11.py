def nhap():
    ho_ten = input("Nhập họ tên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, toan, ly, hoa
def tinh_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3
def xuat(ho_ten, toan, ly, hoa, dtb):
    print("\n--- KẾT QUẢ ---")
    print("Họ tên:", ho_ten)
    print("Toán:", toan)
    print("Lý:", ly)
    print("Hóa:", hoa)
    print("Điểm trung bình:", round(dtb, 2))
ho_ten, toan, ly, hoa = nhap()
dtb = tinh_trung_binh(toan, ly, hoa)
xuat(ho_ten, toan, ly, hoa, dtb)