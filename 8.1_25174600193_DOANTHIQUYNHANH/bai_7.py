def ucln(a, b):
    while b:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return a * b // ucln(a, b)

a, b = map(int, input("Nhập a, b: ").split())
print(f"BCNN({a},{b}) = {bcnn(a,b)}")
a, b = map(int, input("Nhập a, b: ").split())
print(f"UCLN({a},{b}) = {ucln(a,b)}")

def rut_gon_phan_so(tu, mau):
    u = ucln(tu, mau)
    return tu // u, mau // u

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
tu_moi, mau_moi = rut_gon_phan_so(tu, mau)
print(f"Phân số sau rút gọn: {tu_moi}/{mau_moi}")
def tim_min_max(danh_sach):
    return min(danh_sach), max(danh_sach)

n = int(input("Nhập số lượng phần tử: "))
ds = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(n)]
min_val, max_val = tim_min_max(ds)
print(f"Số nhỏ nhất: {min_val}, Số lớn nhất: {max_val}")