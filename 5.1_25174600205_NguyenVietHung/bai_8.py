lst = [0] * 100
n = 0

while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    lst[n] = x
    n += 1

# a
x = int(input("Tìm giá trị x: "))
found = -1

for i in range(n):
    if lst[i] == x:
        found = i
        break

if found != -1:
    print("Vị trí:", found)
else:
    print("Không tìm thấy")

# b
if found != -1:
    new = int(input("Nhập giá trị mới: "))
    lst[found] = new

print("List sau sửa:")
for i in range(n):
    print(lst[i], end=" ")

# c
y = int(input("\nNhập y: "))
pos = int(input("Vị trí (0 đầu, n cuối): "))

for i in range(n, pos, -1):
    lst[i] = lst[i-1]

lst[pos] = y
n += 1

print("List sau thêm:")
for i in range(n):
    print(lst[i], end=" ")

# d
for i in range(n):
    for j in range(i+1, n):
        if lst[i] < lst[j]:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp

print("\nList sau sắp xếp:")
for i in range(n):
    print(lst[i], end=" ")

# e
pos = int(input("\nNhập vị trí cần xóa: "))

for i in range(pos, n-1):
    lst[i] = lst[i+1]

n -= 1

print("List sau xóa:")
for i in range(n):
    print(lst[i], end=" ")