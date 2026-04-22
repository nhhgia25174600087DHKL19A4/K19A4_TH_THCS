def is_nhuan(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def so_ngay_trong_thang(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_nhuan(year) else 28
    return 0

y = int(input("Nhập năm: "))
m = int(input("Nhập tháng: "))
print(f"Năm {y} {'nhuận' if is_nhuan(y) else 'không nhuận'}")
print(f"Tháng {m} năm {y} có {so_ngay_trong_thang(m, y)} ngày")