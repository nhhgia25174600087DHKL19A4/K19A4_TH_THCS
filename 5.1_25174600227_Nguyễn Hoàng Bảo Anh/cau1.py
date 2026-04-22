n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

ds_binh_phuong = []
for i in range(1, n + 1):
    ds_binh_phuong = ds_binh_phuong + [i * i]

if m >= n:
    print("Mục đầu tiên:", ds_binh_phuong)
else:
    print("Mục đầu tiên:", ds_binh_phuong[:m])