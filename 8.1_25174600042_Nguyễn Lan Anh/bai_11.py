def diem_tb(toan, ly, hoa):
    return (toan + ly + hoa) / 3

ten = input("Họ tên: ")
toan = float(input("Toán: "))
ly = float(input("Lý: "))
hoa = float(input("Hóa: "))

tb = diem_tb(toan, ly, hoa)

print("Họ tên:", ten)
print("Điểm TB:", tb)