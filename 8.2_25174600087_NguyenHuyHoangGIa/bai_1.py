def so_ngay_trong_thang(thang, nam):
    la_nam_nhuan = False
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        la_nam_nhuan = True
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if la_nam_nhuan:
            return 29
        else:
            return 28
    else:
        return -1
if __name__ == "__main__":
    t = int(input("Nhập tháng: "))
    n = int(input("Nhập năm: "))
    ngay = so_ngay_trong_thang(t, n)
    if ngay != -1:
        print(f"Số ngày trong tháng {t} năm {n} là: {ngay}")
    else:
        print("Tháng không hợp lệ!")