def tim_ucln(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
def tim_bcnn(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // tim_ucln(a, b)
def rut_gon_phan_so():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    if mau == 0:
        print("Lỗi")
        return     
    ucln = tim_ucln(tu, mau)
    tu_rut_gon = tu // ucln
    mau_rut_gon = mau // ucln
    print(f"Phân số rút gọn là: {tu_rut_gon}/{mau_rut_gon}")
def tim_min_max():
    n = int(input("Nhập số lượng phần tử n: "))
    if n <= 0:
        print("n phải lớn hơn 0")
        return      
    gia_tri_min = 0
    gia_tri_max = 0
    for i in range(n):
        so = int(input(f"Nhập số thứ {i+1}: "))
        if i == 0:
            gia_tri_min = so
            gia_tri_max = so
        else:
            if so < gia_tri_min:
                gia_tri_min = so
            if so > gia_tri_max:
                gia_tri_max = so     
    print(f"Số nhỏ nhất là: {gia_tri_min}")
    print(f"Số lớn nhất là: {gia_tri_max}")
print("UCLN của 12 và 18 là:", tim_ucln(12, 18))
print("BCNN của 12 và 18 là:", tim_bcnn(12, 18))
rut_gon_phan_so()
tim_min_max()