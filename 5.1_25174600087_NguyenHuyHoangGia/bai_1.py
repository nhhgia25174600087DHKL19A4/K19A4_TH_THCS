# Nhập dữ liệu
n = int(input("Nhap n: "))
m = int(input("Nhap m: "))
danh_sach_bp = []
for i in range(1, n + 1):
    danh_sach_bp.append(i**2)
if m >= n:
    print("Ket qua:", danh_sach_bp)
else:
    print("Ket qua:", danh_sach_bp[:m])