n = int(input("Nhập số phần tử: "))
ds = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    ds.append(x)
bp = list(map(lambda x: x * x, ds))
print("Danh sách ban đầu:", ds)
print("Danh sách bình phương:", bp)