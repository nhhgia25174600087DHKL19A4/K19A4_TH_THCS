import math
#tròn
def hinh_tron():
    r = float(input("Nhập bán kính r: "))
    if r <= 0:
        print("Bán kính phải > 0")
        return
    chu_vi = 2 * math.pi * r
    dien_tich = math.pi * r * r
    print("Chu vi:", round(chu_vi, 2))
    print("Diện tích:", round(dien_tich, 2))
#vuông
def hinh_vuong():
    a = float(input("Nhập cạnh a: "))
    if a <= 0:
        print("Cạnh phải > 0")
        return
    chu_vi = 4 * a
    dien_tich = a * a
    print("Chu vi:", chu_vi)
    print("Diện tích:", dien_tich)
#chữ nhật    
def hinh_chu_nhat():
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    if a <= 0 or b <= 0:
        print("Chiều dài và rộng phải > 0")
        return
    chu_vi = 2 * (a + b)
    dien_tich = a * b
    print("Chu vi:", chu_vi)
    print("Diện tích:", dien_tich)
#tam giác    
def hinh_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    if a <= 0 or b <= 0 or c <= 0:
        print("Các cạnh phải > 0")
        return
    if a + b <= c or a + c <= b or b + c <= a:
        print("Không phải tam giác hợp lệ")
        return   
    chu_vi = a + b + c
    p = chu_vi / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    print("Chu vi:", chu_vi)
    print("Diện tích:", round(dien_tich, 2))
#menu
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Hình tròn")
        print("2. Hình vuông")
        print("3. Hình chữ nhật")
        print("4. Hình tam giác")
        print("0. Thoát")
        chon = input("Chọn: ")
        if chon == "1":
            hinh_tron()
        elif chon == "2":
            hinh_vuong()
        elif chon == "3":
            hinh_chu_nhat()
        elif chon == "4":
            hinh_tam_giac()
        elif chon == "0":
            print("Thoát chương trình")
            break
        else:
            print("Chọn không hợp lệ!")
menu()