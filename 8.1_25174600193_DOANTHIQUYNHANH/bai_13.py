def nhap_nv():
    ten = input("Họ tên: ")
    que = input("Quê quán: ")
    tham_nien = int(input("Thâm niên công tác (năm): "))
    return ten, que, tham_nien

def tinh_luong(tham_nien):
    return 5000000 + tham_nien * 500000

def xuat_nv(ten, que, tham_nien, luong):
    print(f"Họ tên: {ten}, Quê: {que}, Thâm niên: {tham_nien} năm, Lương: {luong} VND")

ten, que, tn = nhap_nv()
luong = tinh_luong(tn)
xuat_nv(ten, que, tn, luong)