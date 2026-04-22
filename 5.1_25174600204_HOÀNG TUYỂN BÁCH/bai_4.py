
while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    else:
        print("Lỗi, Yêu cầu 0 < m < n. Nhập lại.")
a = []
for i in range(m, n + 1, 2):
    a.append(i)
tong = 0
for i in range(len(a)):
    tong = tong + a[i]
print("Danh sách:", a)
print("Tổng:", tong)