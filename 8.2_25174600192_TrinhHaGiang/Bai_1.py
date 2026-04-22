def nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False
def so_ngay_trong_thang(m, y):
    if m < 1 or m > 12:
        return -1  # tháng không hợp lệ
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    else:  # tháng 2
        if nam_nhuan(y):
            return 29
        else:
            return 28
def main():
    m = int(input("Nhập tháng: "))
    y = int(input("Nhập năm: "))
    ngay = so_ngay_trong_thang(m, y)
    if ngay == -1:
        print("Tháng không hợp lệ.")
    else:
        print(f"Tháng {m} năm {y} có {ngay} ngày.")
main()
