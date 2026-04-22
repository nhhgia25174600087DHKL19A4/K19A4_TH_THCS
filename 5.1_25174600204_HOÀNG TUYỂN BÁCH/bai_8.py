# a
x = int(input("Nhập giá trị x cần tìm: "))
found = False
for i in range(len(lst)):
    if lst[i] == x:
        print(f"Phần tử {x} có vị trí đầu tiên là: {i}")
        found = True
        break
if not found:
    print(f"Không tìm thấy giá trị {x} trong danh sách.")
# b
if found:
    vt = int(input(f"Nhập vị trí muốn chỉnh sửa (0 → {len(lst)-1}): "))
    if 0 <= vt < len(lst):
        new_val = int(input(f"Nhập giá trị mới thay cho {lst[vt]}: "))
        lst[vt] = new_val
        print("Danh sách sau khi chỉnh sửa:", lst)
    else:
        print("Vị trí không hợp lệ.")
# c
y = int(input("Nhập giá trị y muốn thêm: "))
vt = int(input(f"Nhập vị trí muốn thêm (0 → {len(lst)}): "))
if 0 <= vt <= len(lst):
    lst.insert(vt, y)
else:
    print("Vị trí không hợp lệ, thêm vào cuối.")
    lst.append(y)
print("Danh sách sau khi thêm:", lst)
# d
print("Danh sách trước khi sắp xếp:", lst)
for i in range(len(lst)-1):
    max_idx = i
    for j in range(i+1, len(lst)):
        if lst[j] > lst[max_idx]:
            max_idx = j
    if max_idx != i:
        lst[i], lst[max_idx] = lst[max_idx], lst[i]

print("Danh sách sau khi sắp xếp giảm dần:", lst)