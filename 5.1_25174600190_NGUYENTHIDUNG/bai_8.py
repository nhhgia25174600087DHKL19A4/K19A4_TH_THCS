lst = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    lst.append(x)
   #a  
find_x = int(input("Nhập x: "))
if find_x in lst:
    pos = lst.index(find_x)
    print("Vị trí:", pos)

    # b
    new_val = int(input("Nhập giá trị mới: "))
    lst[pos] = new_val
    print("Sau sửa:", lst)
else:
    print("Không tìm thấy")

    # c
y = int(input("Nhập y: "))
lst.append(y)

    # d
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Sau sắp xếp:", lst)

    # e
del_index = int(input("Nhập vị trí cần xóa: "))
if 0 <= del_index < len(lst):
    lst.pop(del_index)

print("Sau xóa:", lst)