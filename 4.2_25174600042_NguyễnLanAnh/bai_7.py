while True:
    print("\n.MENU ĐỒ UỐNG")
    print("1.Cafe   2.Cam vắt   3.Nước ép cà rốt   4.Nước lọc   5.Nước dừa   0.Thoát")

    chon = int(input("Chọn đồ uống: "))

    if chon == 1:
        print("Bạn chọn Cafe")
    elif chon == 2:
        print("Bạn chọn Cam vắt")
    elif chon == 3:
        print("Bạn chọn Nước ép cà rốt")
    elif chon == 4:
        print("Bạn chọn Nước lọc")
    elif chon == 5:
        print("Bạn chọn Nước dừa")
    else:
        print("Thoát chương trình")
        break