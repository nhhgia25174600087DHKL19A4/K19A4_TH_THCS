def la_nam_nhuan(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def so_ngay_trong_thang(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if la_nam_nhuan(y):
            return 29
        else:
            return 28
    else:
        return -1
m = int(input("Nhap thang: "))
y = int(input("Nhap nam: "))
kq = so_ngay_trong_thang(m, y)
if kq == -1:
    print("Thang khong hop le")
else:
    print("So ngay:", kq)