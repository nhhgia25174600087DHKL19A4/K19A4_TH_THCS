a = [0]*1000  
n = 0
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a[n] = x
    n += 1

# a
for i in range(n-1, -1, -1):
    a[i+3] = a[i]

a[0] = 1
a[1] = 2
a[2] = 3
n += 3


a[n] = 1
a[n+1] = 2
a[n+2] = 3
n += 3


if n >= 4:
    for i in range(n-1, 3, -1):
        a[i+3] = a[i]
    a[4] = 1
    a[5] = 2
    a[6] = 3
    n += 3

print("Danh sách sau khi chèn:", end=" ")
for i in range(n):
    print(a[i], end=" ")
print()

# b
k = int(input("Nhập vị trí k cần xóa (0-based): "))

if 0 <= k < n:
    for i in range(k, n-1):
        a[i] = a[i+1]
    n -= 1
else:
    print("Vị trí k không hợp lệ")

print("Danh sách sau khi xóa:", end=" ")
for i in range(n):
    print(a[i], end=" ")
print()

# c
for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Danh sách tăng dần:", end=" ")
for i in range(n):
    print(a[i], end=" ")
print()


for i in range(n-1):
    for j in range(n-1-i):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Danh sách giảm dần:", end=" ")
for i in range(n):
    print(a[i], end=" ")
print()

t = tuple(a[:n])
print("Tuple:", t)