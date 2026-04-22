m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

while m <= 0 or m >= n:
    print("Nhập sai! Yêu cầu 0 < m < n")
    m = int(input("Nhập lại m: "))
    n = int(input("Nhập lại n: "))

ds = []
i = m

while i <= n and len(ds) < 100:
    ds.append(i)
    i = i + 2

tong = 0
for x in ds:
    tong = tong + x

print("Danh sách là:", ds)
print("Tổng là:", tong)