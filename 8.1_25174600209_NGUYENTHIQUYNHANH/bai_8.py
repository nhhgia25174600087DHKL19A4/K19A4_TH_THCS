# Hàm tính toán cho hình tròn
def hinh_tron():
    r = float(input("Nhập bán kính hình tròn: "))
    if r > 0:
        cv = 2 * 3.14 * r
        dt = 3.14 * r * r
        print("Hình tròn: Chu vi = {}, Diện tích = {}".format(cv, dt))
    else:
        print("Bán kính phải lớn hơn 0!")
def hinh_vuong():
    a = float(input("Nhập cạnh hình vuông: "))
    if a > 0:
        cv = 4 * a
        dt = a * a
        print("Hình vuông: Chu vi = {}, Diện tích = {}".format(cv, dt))
    else:
        print("Cạnh phải lớn hơn 0!")
def hinh_chu_nhat():
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    if dai > 0 and rong > 0:
        cv = (dai + rong) * 2
        dt = dai * rong
        print("Hình chữ nhật: Chu vi = {}, Diện tích = {}".format(cv, dt))
    else:
        print("Các cạnh phải lớn hơn 0!")
def hinh_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        cv = a + b + c
        p = cv / 2
        dt = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print("Hình tam giác: Chu vi = {}, Diện tích = {}".format(cv, dt))
    else:
        print("Ba cạnh không tạo thành một tam giác hợp lệ!")
def bai_8():
    print("--- Chương trình tính Chu vi & Diện tích ---")
    print("1. Hình tròn")
    print("2. Hình vuông")
    print("3. Hình chữ nhật")
    print("4. Hình tam giác")
    chon = input("Chọn hình muốn tính (1-4): ")
    if chon == '1': hinh_tron()
    elif chon == '2': hinh_vuong()
    elif chon == '3': hinh_chu_nhat()
    elif chon == '4': hinh_tam_giac()
    else: print("Lựa chọn không hợp lệ!")
bai_8()