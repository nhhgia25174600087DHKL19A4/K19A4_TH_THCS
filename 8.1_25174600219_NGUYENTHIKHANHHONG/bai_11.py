def nhap():
    ten = input("Nhập họ tên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ten, toan, ly, hoa

# Hàm tính trung bình
def tinh_tb(toan, ly, hoa):
    return (toan + ly + hoa) / 3

# Hàm xuất
def xuat(ten, tb):
    print("Họ tên:", ten)
    print("Điểm trung bình:", tb)

# Chương trình chính 
ten, toan, ly, hoa = nhap()
tb = tinh_tb(toan, ly, hoa)
xuat(ten, tb)