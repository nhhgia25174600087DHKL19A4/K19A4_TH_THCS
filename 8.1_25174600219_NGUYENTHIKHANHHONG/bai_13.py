# Hàm kiểm tra năm nhuận
def nam_nhuan(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False

# Hàm số ngày của tháng
def so_ngay_thang(m, y):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    elif m == 2:
        if nam_nhuan(y):
            return 29
        else:
            return 28
    else:
        return 0 


# Chương trình chính 
y = int(input("Nhập năm: "))
m = int(input("Nhập tháng: "))

# kiểm tra năm nhuận
if nam_nhuan(y):
    print(y, "là năm nhuận")
else:
    print(y, "không phải năm nhuận")

# số ngày trong tháng
ngay = so_ngay_thang(m, y)
if ngay == 0:
    print("Tháng không hợp lệ")
else:
    print("Tháng", m, "có", ngay, "ngày")