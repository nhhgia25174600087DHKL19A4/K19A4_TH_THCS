n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
danh_sach_goc = []
for i in range(1, n+1):
    danh_sach_goc.append(i**2)
if m >= n:
    ket_qua = []
else:
    ket_qua = danh_sach_goc[:m]
print("Kết quả:", ket_qua)