def ham_sinh_vien():
    ten = input("nhập họ tên SV: ")
    toan = float(input("điểm Toán: "))
    ly = float(input("điểm Lý: "))
    hoa = float(input("điểm Hóa: "))
    return {"ten": ten, "toan": toan, "ly": ly, "hoa": hoa}
def tinh_diem_trung_binh(sv):
    return (sv["toan"] + sv["ly"] + sv["hoa"]) / 3
def diem_trung_binh(sv):
    dtb = tinh_diem_trung_binh(sv)
    print(f"Sinh viên: {sv['ten']} | ĐTB: {dtb:.2f}")
ham_sinh_vien()
tinh_diem_trung_binh()
diem_trung_binh()
