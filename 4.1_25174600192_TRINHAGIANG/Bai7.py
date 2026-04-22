while True:
    print("\n--- MENU ---")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")
    
    chon = int(input("Chọn chức năng: "))
    
    if chon == 0:
        print("Thoát chương trình.")
        break
    
    if chon in [1, 2, 3, 4]:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        
        if chon == 1:
            print("Kết quả:", a + b)
        elif chon == 2:
            print("Kết quả:", a - b)
        elif chon == 3:
            print("Kết quả:", a * b)
        elif chon == 4:
            if b != 0:
                print("Kết quả:", a / b)
            else:
                print("Lỗi: Không chia được cho 0!")
    else:
        print("Chọn sai, vui lòng nhập lại!")