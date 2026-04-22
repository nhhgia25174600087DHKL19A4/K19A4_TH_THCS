def nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False
def so_ngay(m, y):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m == 2:
        if nam_nhuan(y):
            return 29
        return 28
y = int(input("Năm: "))
m = int(input("Tháng: "))
print("Năm nhuận:", nam_nhuan(y))
print("Số ngày:", so_ngay(m,y))