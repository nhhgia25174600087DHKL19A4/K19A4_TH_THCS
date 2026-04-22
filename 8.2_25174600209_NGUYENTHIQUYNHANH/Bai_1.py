def so_ngay_trong_thang():
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        print("Tháng {} năm {} có 31 ngày".format(thang, nam))
    elif thang in [4, 6, 9, 11]:
        print("Tháng {} năm {} có 30 ngày".format(thang, nam))
    elif thang == 2:
        if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
            print("Tháng 2 năm {} có 29 ngày (Năm nhuận)".format(nam))
        else:
            print("Tháng 2 năm {} có 28 ngày".format(nam))
    else:
        print("Tháng không hợp lệ!")
so_ngay_trong_thang()