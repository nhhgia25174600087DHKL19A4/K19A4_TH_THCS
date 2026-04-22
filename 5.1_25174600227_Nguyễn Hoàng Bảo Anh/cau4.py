m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

ds_100 = []
current = m

while len(ds_100) < 100 and current <= n:
    ds_100 = ds_100 + [current]
    current = current + 2

tong = 0
for so in ds_100:
    tong = tong + so

print("Danh sách:", ds_100)
print("Tổng của danh sách:", tong)