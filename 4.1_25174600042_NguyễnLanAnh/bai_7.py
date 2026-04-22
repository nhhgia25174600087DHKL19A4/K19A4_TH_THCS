while True:
    print("\n1.Cộng   2.Trừ   3.Nhân   4.Chia   0.Thoát")
    chon = int(input("Chọn: "))

    if chon == 0:
        break
    a = float(input("a: "))
    b = float(input("b:"))

    if chon == 1:
        print(a + b)
    elif chon == 2:
        print(a - b)
    elif chon == 3:
        print(a * b)
    elif chon == 4:
        print(a / b if b != 0 else "Không chia được")
        