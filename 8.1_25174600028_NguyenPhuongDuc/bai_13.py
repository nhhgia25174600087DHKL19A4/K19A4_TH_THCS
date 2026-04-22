def ham_kiem_tra_nam_nhuan(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def so_ngay_trong_thang(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29 if ham_kiem_tra_nam_nhuan(y) else 28
    else:
        return "Tháng không hợp lệ"
