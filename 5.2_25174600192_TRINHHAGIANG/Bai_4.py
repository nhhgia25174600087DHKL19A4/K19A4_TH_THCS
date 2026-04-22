# Nhập danh sách (dừng khi nhập 0)
a = []
x = int(input("Nhập số (0 để dừng): "))

while x != 0:
    a.append(x)
    x = int(input("Nhập số (0 để dừng): "))

print("Danh sách ban đầu:", a)

# a
b = [1, 2, 3]

a1 = b + a
a2 = a + b
a3 = a.copy()
if len(a3) >= 5:
    a3 = a3[:4] + b + a3[4:]
else:
    a3 = a3 + b

print("Chèn đầu:", a1)
print("Chèn cuối:", a2)
print("Chèn vị trí 5:", a3)

# b. Xóa phần tử thứ k
k = int(input("Nhập vị trí cần xóa: "))

if 0 <= k < len(a):
    a.pop(k)
else:
    print("Vị trí không hợp lệ")

print("Sau khi xóa:", a)

# c

a_tang = a.copy()
for i in range(len(a_tang)):
    for j in range(i + 1, len(a_tang)):
        if a_tang[i] > a_tang[j]:
            temp = a_tang[i]
            a_tang[i] = a_tang[j]
            a_tang[j] = temp
a_giam = a.copy()
for i in range(len(a_giam)):
    for j in range(i + 1, len(a_giam)):
        if a_giam[i] < a_giam[j]:
            temp = a_giam[i]
            a_giam[i] = a_giam[j]
            a_giam[j] = temp

print("Tăng dần:", a_tang)
print("Giảm dần:", a_giam)