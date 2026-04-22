def so_ngay_trong_thang():
    m = int(input("Tháng: "))
    y = int(input("Năm: "))
    
    # Năm nhuận
    nhuan = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    
    if m in [4,6,9,11]: return 30
    if m == 2: return 29 if nhuan else 28
    return 31 if 1 <= m <= 12 else 0

print("Số ngày:", so_ngay_trong_thang())