def so_ngay_trong_thang(thang, nam):
    if thang < 1 or thang > 12:
        return 0
    # tháng có 31 ngày
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # tháng có 30 ngày
    if thang in [4, 6, 9, 11]:
        return 30
    # tháng 2 (xét năm nhuận)
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return 29
    else:
        return 28
# Chương trình chính 
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
kq = so_ngay_trong_thang(thang, nam)
if kq == 0:
    print("Tháng không hợp lệ")
else:
    print("Số ngày trong tháng:", kq)