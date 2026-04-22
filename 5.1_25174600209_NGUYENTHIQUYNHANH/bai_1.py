n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
danh_sach_binh_phuong = []
for i in range(1, n+1):
    danh_sach_binh_phuong.append(i**2)
if m >= n:
    print("Danh sách kết quả:",danh_sach_binh_phuong)
else:
    ket_qua = danh_sach_binh_phuong[:m]
    print(f"{m} mục đầu tiên trong danh sách là:", ket_qua)