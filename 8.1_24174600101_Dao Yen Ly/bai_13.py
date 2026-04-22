y = int(input("Nhap nam: "))
m = int(input("Nhap thang: "))

# kiem tra nam nhuan:
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Nam nhuan")
    nhuan = True
else:
    print("Khong phai nam nhuan")
    nhuan = False

# kiem tra thang:
if m < 1 or m > 12:
    print("Thang khong hop le")
else:
    if m == 2:
        if nhuan:
            print("So ngay: 29")
        else:
            print("So ngay: 28")
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print("So ngay: 30")
    else:
        print("So ngay: 31")