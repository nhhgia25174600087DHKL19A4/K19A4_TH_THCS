while True:
    x = input("Nhập số: ")
    for i in x:
        if i == '.':
            print("Số thập phân, dừng!")
            exit()
    x = int(x)
    if x < 0:
        print("Số âm, dừng!")
        break