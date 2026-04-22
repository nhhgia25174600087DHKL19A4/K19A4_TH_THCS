# Nhập n
n = int(input("Nhập n: "))

# Nhập danh sách đúng n phần tử
a = []
for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

# a. Tính tổng
tong = 0
for i in range(n):
    tong += a[i]
print("a) Tong =", tong)

# b. Đếm và tính tổng số dương
dem = 0
tong_duong = 0
for i in range(n):
    if a[i] > 0:
        dem += 1
        tong_duong += a[i]

print("b) So duong =", dem)
print("   Tong duong =", tong_duong)

# c. Vị trí phần tử âm đầu tiên
vt_am = -1
for i in range(n):
    if a[i] < 0:
        vt_am = i
        break
print("c) VT am dau =", vt_am)

# d. Vị trí phần tử dương cuối cùng
vt_duong = -1
for i in range(n-1, -1, -1):
    if a[i] > 0:
        vt_duong = i
        break
print("d) VT duong cuoi =", vt_duong)

# e. Phần tử lớn nhất và vị trí cuối
if n > 0:
    max_val = a[0]
    for i in range(1, n):
        if a[i] > max_val:
            max_val = a[i]

    vt_max = -1
    for i in range(n-1, -1, -1):
        if a[i] == max_val:
            vt_max = i
            break

    print("e) Max =", max_val)
    print("   VT max cuoi =", vt_max)
else:
    print("Danh sách rỗng")