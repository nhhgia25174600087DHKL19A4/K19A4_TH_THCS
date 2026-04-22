def hinh_tron():
    r = float(input("Nhập bán kính hình tròn: "))
    if r <= 0:
        print("Bán kính phải lớn hơn 0")
        return
    pi = 3.14159
    chu_vi = 2 * pi * r
    dien_tich = pi * (r ** 2)
    print(f"Chu vi: {chu_vi}, Diện tích: {dien_tich}")
def hinh_vuong():
    a = float(input("Nhập cạnh hình vuông: "))
    if a <= 0:
        print("Cạnh phải lớn hơn 0")
        return
    chu_vi = 4 * a
    dien_tich = a ** 2
    print(f"Chu vi: {chu_vi}, Diện tích: {dien_tich}")
def hinh_chu_nhat():
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    if a <= 0 or b <= 0:
        print("Các cạnh phải lớn hơn 0")
        return
    chu_vi = 2 * (a + b)
    dien_tich = a * b
    print(f"Chu vi: {chu_vi}, Diện tích: {dien_tich}")
def hinh_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        chu_vi = a + b + c
        p = chu_vi / 2
        dien_tich = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(f"Chu vi: {chu_vi}, Diện tích: {dien_tich}")
    else:
        print("Không hợp lệ")
hinh_tron()
hinh_vuong()
hinh_chu_nhat()
hinh_tam_giac()