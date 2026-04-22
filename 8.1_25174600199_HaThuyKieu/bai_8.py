import math

while True:
    print("\n===== MENU =====")
    print("1. Hình tròn")
    print("2. Hình vuông")
    print("3. Hình chữ nhật")
    print("4. Hình tam giác")
    print("0. Thoát")
    chon = input("Chọn: ")
#Hình_tròn
    if chon == "1":
        r = float(input("Nhập bán kính: "))
        if r <= 0:
            print("Không hợp lệ!")
        else:
            print("Chu vi =", 2 * math.pi * r)
            print("Diện tích =", math.pi * r * r)
#Hình_vuông
    elif chon == "2":
        a = float(input("Nhập cạnh: "))
        if a <= 0:
            print("Không hợp lệ!")
        else:
            print("Chu vi =", 4 * a)
            print("Diện tích =", a * a)
#Hình_cn
    elif chon == "3":
        a = float(input("Nhập chiều dài: "))
        b = float(input("Nhập chiều rộng: "))
        if a <= 0 or b <= 0:
            print("Không hợp lệ!")
        else:
            print("Chu vi =", 2 * (a + b))
            print("Diện tích =", a * b)
#Hình_tam_giac
    elif chon == "4":
        a = float(input("Nhập cạnh a: "))
        b = float(input("Nhập cạnh b: "))
        c = float(input("Nhập cạnh c: "))
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            print("Không hợp lệ!")
        else:
            p = (a + b + c) / 2
            print("Chu vi =", a + b + c)
            print("Diện tích =", math.sqrt(p * (p - a) * (p - b) * (p - c)))
    elif chon == "0":
        print("Kết thúc!")
        break
    else:
        print("Chọn sai!")