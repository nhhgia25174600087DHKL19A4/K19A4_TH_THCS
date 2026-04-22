def la_nam_nhuan(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    return False

def so_ngay_trong_thang(m, y):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    elif m == 2:
        if la_nam_nhuan(y):
            return 29
        else:
            return 28
    else:
        return 0

m = int(input("Nhap thang: "))
y = int(input("Nhap nam: "))
kq = so_ngay_trong_thang(m, y)
if kq == 0:
    print("Thang khong hop le")
else:
    print("So ngay:", kq)