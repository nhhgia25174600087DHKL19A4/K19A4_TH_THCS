n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

ds_binh_phuong = []
for i in range(1, n + 1):
    ds_binh_phuong.append(i ** 2)

# In kết quả
if m >= n:
    print("Danh sách kết quả là:", ds_binh_phuong)
else:
    print(f"{m} phần tử đầu tiên là:", ds_binh_phuong[:m])