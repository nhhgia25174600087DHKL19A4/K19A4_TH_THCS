def in_day():
    n = int(input("Nhập số phần tử: "))
    dem = 0
    for i in range(n):
        x = int(input("Nhập số: "))
        print(x, end=" ")
        dem = dem + 1
    print("Số lượng là:", dem)

in_day()