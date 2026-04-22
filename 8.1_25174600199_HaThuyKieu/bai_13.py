nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng: "))
def kiem_tra_nam_nhuan(nam):
    return nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)

def so_ngay_thang(thang, nam):
    ngay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if kiem_tra_nam_nhuan(nam):
        ngay[1] = 29
        
    return ngay[thang - 1]

if kiem_tra_nam_nhuan(nam):
    print("Đây là năm nhuận")
else:
    print("Đây không phải năm nhuận")

print("Số ngày của tháng", thang, "là:", so_ngay_thang(thang, nam))