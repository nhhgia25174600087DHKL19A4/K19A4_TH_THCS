def nhap():
    ho_ten = input("Nhập họ tên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, toan, ly, hoa

def tinh_tb(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat(ho_ten, toan, ly, hoa, tb):
    print("Họ tên:", ho_ten)
    print("Toán:", toan)
    print("Lý:", ly)
    print("Hóa:", hoa)
    print("Trung bình:", tb)

def main():
    ho_ten, toan, ly, hoa = nhap()
    tb = tinh_tb(toan, ly, hoa)
    xuat(ho_ten, toan, ly, hoa, tb)

main()