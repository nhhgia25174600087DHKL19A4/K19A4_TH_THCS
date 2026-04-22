lst = []
while True:
    x = int(input("Nhập (0 để dừng): "))
    if x == 0:
        break
    lst.append(x)

print("Danh sách:", lst)

# a
x = int(input("Tìm x: "))
vi_tri = -1
for i in range(len(lst)):
    if lst[i] == x:
        vi_tri = i
        break

if vi_tri != -1:
    print("Vị trí:", vi_tri)
else:
    print("Không có")

# b
if vi_tri != -1:
    gia_tri_moi = int(input("Giá trị mới: "))
    lst[vi_tri] = gia_tri_moi
    print(lst)

# c
y = int(input("Nhập y: "))
lst.append(y)
print(lst)

# d
print("Trước:", lst)
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] < lst[j]:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
print("Sau:", lst)

# e
if len(lst) > 0:
    del lst[0]
print(lst)