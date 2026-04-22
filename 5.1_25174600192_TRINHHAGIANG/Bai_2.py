n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

ds_binh_phuong = []
for i in range(1, n + 1):
    ds_binh_phuong.append(i ** 2)

if m >= n:
    print("Danh sách kết quả là: Rỗng")
else:
    print("Danh sách sau khi bỏ", m, "phần tử đầu là:", ds_binh_phuong[m:])