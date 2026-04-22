n = int(input("Nhập số phần tử n: "))
ds = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    ds.append(x)
print("List ban đầu:", ds)
ds_binh_phuong = list(map(lambda x: x**2, ds))
print("List bình phương:", ds_binh_phuong)