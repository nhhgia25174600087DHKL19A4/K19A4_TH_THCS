#a
ds = []
for i in range(1, 101):
    if i % 2 == 0:
        ds.append(i)
print("Danh sách số chẵn từ 1 đến 100 là:")
print(ds)

#b

n = int(input("Nhập số phần tử: "))
ds = []

for i in range(n):
    x = int(input("Nhập phần tử: "))
    ds.append(x)

tong = 0

for i in ds:
    if i % 2 == 0:
        tong += i

print("Tổng các số chẵn là:", tong)