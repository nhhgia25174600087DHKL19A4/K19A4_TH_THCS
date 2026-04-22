def so_ngay_trong_thang(thang, nam):
    nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
    
    if thang in [1,3,5,7,8,10,12]:
        return 31
    elif thang in [4,6,9,11]:
        return 30
    elif thang == 2:
        return 29 if nam_nhuan else 28
    else:
        return -1  


t = int(input("Tháng: "))
n = int(input("Năm: "))
kq = so_ngay_trong_thang(t, n)
print("Số ngày:", kq if kq != -1 else "Không hợp lệ")