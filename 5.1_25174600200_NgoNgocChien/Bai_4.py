m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
a = []
for i in range(m, n + 1, 2):
    a.append(i)
print("Danh sách:", a)
tong = 0
for i in a:
    tong += i
print("Tổng:", tong)        