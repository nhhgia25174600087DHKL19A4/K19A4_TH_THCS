def nhap_thong_tin():
    ho_ten = input("Nhập họ tên sinh viên: ")
    diem_toan = float(input("Nhập điểm Toán: "))
    diem_ly = float(input("Nhập điểm Lý: "))
    diem_hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa
def tinh_diem_tb(t, l, h):
    dtb = (t + l + h) / 3
    return dtb
def xuat_ket_qua(name, t, l, h, dtb):
    print("\n--- Kết quả học tập ---")
    print("Họ tên: {}".format(name))
    print("Điểm Toán: {}, Lý: {}, Hóa: {}".format(t, l, h))
    print("Điểm trung bình: {:.2f}".format(dtb))
def bai_11():
    ten, toan, ly, hoa = nhap_thong_tin()
    dtb = tinh_diem_tb(toan, ly, hoa)
    xuat_ket_qua(ten, toan, ly, hoa, dtb)
bai_11()