while True:
    x = float(input("Nhập số: "))
    if x < 0:
        print("Số âm -> dừng")
        break
    if x != int(x):
        print("Số thập phân -> dừng")
        break
    print("nhập:", int(x))