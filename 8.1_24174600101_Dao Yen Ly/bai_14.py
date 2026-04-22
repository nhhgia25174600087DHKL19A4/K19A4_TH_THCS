n = int(input("Nhap n: "))
ds = []

for i in range(n):
    x = int(input("Nhap so: "))
    ds.append(x)

ds_binh_phuong = list(map(lambda x: x * x, ds))

print("Danh sach binh phuong:", ds_binh_phuong)