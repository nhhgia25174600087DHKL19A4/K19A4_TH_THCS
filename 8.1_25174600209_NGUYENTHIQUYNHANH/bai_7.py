def tim_ucln(a, b):
    while b != 0:
        so_du = a % b
        a = b
        b = so_du
    return a
def tim_bcnn(a, b):
    if a == 0 or b == 0:
        return 0
    ucln = tim_ucln(a, b)
    return abs(a * b) // ucln
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
print("UCLN({}, {}) = {}".format(a, b, tim_ucln(a, b)))
print("BCNN({}, {}) = {}".format(a, b, tim_bcnn(a, b)))
#c
def rut_gon_phan_so():
    print("\n--- Câu c: Rút gọn phân số ---")
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    if mau == 0:
        print("Mẫu số phải khác 0!")
        return
    ucln = tim_ucln(abs(tu), abs(mau))
    tu_moi = tu // ucln
    mau_moi = mau // ucln
    print("Phân số sau khi rút gọn: {}/{}".format(tu_moi, mau_moi))
rut_gon_phan_so()
#d
def tim_max_min():
    print("\n--- Câu d: Tìm Max và Min trong n số ---")
    n = int(input("Bạn muốn nhập bao nhiêu số nguyên? n = "))
    if n <= 0:
        print("n phải lớn hơn 0")
        return
    so = int(input("Nhập số thứ 1: "))
    so_max = so
    so_min = so
    for i in range(2, n + 1):
        so = int(input("Nhập số thứ {}: ".format(i)))
        if so > so_max:
            so_max = so
        if so < so_min:
            so_min = so
    print("Số lớn nhất là: {}".format(so_max))
    print("Số nhỏ nhất là: {}".format(so_min))
tim_max_min()