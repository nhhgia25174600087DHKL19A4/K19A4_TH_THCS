#Dùng whike
while True:
    print("----- MENU -----")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")

    chon = int(input("Chọn đồ uống (1-5): "))

    if chon == 1:
        print("Bạn chọn Cafe")
        break
    elif chon == 2:
        print("Bạn chọn Cam vắt")
        break
    elif chon == 3:
        print("Bạn chọn Nước ép cà rốt")
        break
    elif chon == 4:
        print("Bạn chọn Nước lọc")
        break
    elif chon == 5:
        print("Bạn chọn Nước dừa")
        break
    else:
        print("Chọn sai, nhập lại!")

#Dùng for:
for i in range(1): 
    print("----- MENU -----")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")

    chon = int(input("Chọn đồ uống (1-5): "))

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
        print("Chọn sai!")