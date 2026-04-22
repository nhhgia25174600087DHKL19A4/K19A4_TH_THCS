n = int(input("Nhap n: "))
ds = []

for i in range(n):
    ds.append(int(input()))

binh_phuong = list(map(lambda x: x*x, ds))
print(binh_phuong)