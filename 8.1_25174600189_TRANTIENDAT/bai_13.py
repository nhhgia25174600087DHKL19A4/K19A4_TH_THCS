def la_nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False

def so_ngay_trong_thang(m, y):
    if m < 1 or m > 12:
        return "Tháng không hợp lệ"

    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    if m in [4, 6, 9, 11]:
        return 30

    if la_nam_nhuan(y):
        return 29
    else:
        return 28

def main():
    y = int(input("Nhập năm: "))
    m = int(input("Nhập tháng: "))

    if la_nam_nhuan(y):
        print("Năm nhuận")
    else:
        print("Năm không nhuận")

    print("Số ngày:", so_ngay_trong_thang(m, y))

main()