def so_ngay_trong_thang(thang, nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        nhuan = True
    else:
        nhuan = False

    if thang == 2:
        if nhuan:
            return 29
        else:
            return 28
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        return 30
    else:
        return 31

m = int(input("Nhap thang: "))
y = int(input("Nhap nam: "))

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Nam nhuan")
else:
    print("Khong phai nam nhuan")

print("So ngay:", so_ngay_trong_thang(m, y))