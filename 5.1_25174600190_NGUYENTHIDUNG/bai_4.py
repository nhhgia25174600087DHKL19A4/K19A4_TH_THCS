m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

danh_sach = []
hien_tai = m
while hien_tai <= n and len(danh_sach) < 100:
    danh_sach.append(hien_tai)
    hien_tai += 2

tong = sum(danh_sach)
print("Danh sách:", danh_sach)
print("Tổng của danh sách:", tong)