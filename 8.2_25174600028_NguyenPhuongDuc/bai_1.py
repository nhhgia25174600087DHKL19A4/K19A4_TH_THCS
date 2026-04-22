def kiem_tra_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
def so_ngay_trong_thang(thang, nam):
    thang_31 = [1, 3, 5, 7, 8, 10, 12]
    thang_30 = [4, 6, 9, 11]
    
    if thang in thang_31:
        return 31
    elif thang in thang_30:
        return 30
    elif thang == 2:
        if kiem_tra_nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return -1 
print("=== BÀI 1 ===")
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
so_ngay = so_ngay_trong_thang(thang, nam)
if so_ngay != -1:
    print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.\n")
else:
    print("Tháng không hợp lệ!\n")