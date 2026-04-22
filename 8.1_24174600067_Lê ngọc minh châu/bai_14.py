n = int(input("Nhap so luong: "))
ds = []
i = 0
while i < n:
    x = int(input("Nhap so: "))
    ds.append(x)
    i = i + 1

kq = list(map(lambda x: x*x, ds))
print("Danh sach binh phuong:", kq)