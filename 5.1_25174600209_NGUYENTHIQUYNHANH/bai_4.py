while True:
    m = int(input("Nhập m (m > 0): "))
    n = int(input("Nhập n (n > m): "))
    if 0 < m < n:
        break
    print("Lỗi,Nhập lại m và n")
danh_sach = []
so_hien_tai = m
while so_hien_tai <= n and len(danh_sach) < 100:
    danh_sach.append(so_hien_tai)
    so_hien_tai += 2  
tong = sum(danh_sach)
print(f"Danh sách tạo được ({len(danh_sach)} số):", danh_sach)
print("Tổng của các số trong danh sách là:", tong)