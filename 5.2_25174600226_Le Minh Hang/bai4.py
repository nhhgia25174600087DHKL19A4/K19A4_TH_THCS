# Nhập danh sách đến khi gặp 0
a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a.append(x)

# a. Chèn [1,2,3] vào đầu, cuối, vị trí 5
b = [1, 2, 3]

# đầu
a = b + a

# cuối
a = a + b

# vị trí thứ 5 (index 4)
if len(a) >= 4:
    a = a[:4] + b + a[4:]
else:
    a = a + b

print("a. Sau khi chèn:", a)


# b. Xóa phần tử thứ k
k = int(input("Nhập k: "))
if 0 <= k < len(a):
    a = a[:k] + a[k+1:]
else:
    print("k không hợp lệ")

print("b. Sau khi xóa:", a)


# c. Sắp xếp tăng dần (cách cơ bản - đổi chỗ)
# tăng dần
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print("c. Tăng dần:", a)

# giảm dần
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print("   Giảm dần:", a)