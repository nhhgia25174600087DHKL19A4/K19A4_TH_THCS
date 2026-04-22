while True:
    print("\n1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    chon = int(input("Chọn: "))
    if chon == 0:
        print("Thoát chương trình")
        break
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if chon == 1:
        print("kết quả:", a + b)
    elif chon == 2:
        print("kết quả:", a - b)
    elif chon == 3:
        print("kết quả:", a * b)
    elif chon == 4:
        if b != 0:
            print("kết quả:", a / b)   
        else:
            print("Không thể chia cho 0") 
    else:
        print("Lựa chọn không hợp lệ")        