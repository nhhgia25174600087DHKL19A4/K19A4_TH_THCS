n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

day_so_goc = tuple(range(1, n + 1))

ds_binh_phuong = []
for x in day_so_goc:
    ds_binh_phuong.append( x * x)

if m >= n:
    ket_qua = ds_binh_phuong
else:
    ket_qua = ds_binh_phuong[:m]

print("Kết quả là: ", ket_qua)