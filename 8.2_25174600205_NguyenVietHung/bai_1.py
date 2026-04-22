def so_ngay_trong_thang(thang, nam):

    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        return 31

    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        return 30

    elif thang == 2:
        if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
            return 29
        else:
            return 28

    else:
        return "Tháng không hợp lệ"

thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

print("Số ngày trong tháng là:", so_ngay_trong_thang(thang, nam))