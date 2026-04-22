while True:
    print("\n--- MENU PHÉP TOÁN ---")
    print("1. Cộng (+)")
    print("2. Trừ (-)")
    print("3. Nhân (*)")
    print("4. Chia (/)")
    print("0. Thoát")
    chon = input("Chọn chức năng: ")
    if chon == '0':
        break   
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))    
    if chon == '1': print("Kết quả:", a + b)
    elif chon == '2': print("Kết quả:", a - b)
    elif chon == '3': print("Kết quả:", a * b)
    elif chon == '4':
        if b != 0: print("Kết quả:", a / b)
        else: print("Lỗi: Không thể chia cho 0")
    else: print("Lựa chọn không hợp lệ!")