n = int(input("Nhập n: "))
a = [0]*n
for i in range(n):
    a[i] = int(input("Nhập phần tử thứ " + str(i) + ": "))

tong_duong = 0
tong_am = 0
for i in range(n):
    if a[i] > 0:
        tong_duong += a[i]
    elif a[i] < 0:
        tong_am += a[i]

print("Tổng số dương:", tong_duong)
print("Tổng số âm:", tong_am)

t = tuple(a)
print("Tuple:", t)