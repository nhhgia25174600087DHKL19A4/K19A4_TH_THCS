while True:
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")
    print("0. Thoát")
    chon = int(input("Chọn: "))
    if chon == 0:
        break
    for i in range(1):
        if chon == 1:
            print("Cafe")
        elif chon == 2:
            print("Cam vắt")
        elif chon == 3:
            print("Nước ép cà rốt")
        elif chon == 4:
            print("Nước lọc")
        elif chon == 5:
            print("Nước dừa")
        else:
            print("Sai!")