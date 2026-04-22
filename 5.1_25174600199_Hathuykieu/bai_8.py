ds = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    ds.append(x)

print("Danh sách ban đầu:", ds)
#a
x = int(input("Nhập giá trị cần tìm: "))
if x in ds:
    print("Vị trí của", x, "là:", ds.index(x))
else:
    print("Không tìm thấy")
#b
if x in ds:
    new_value = int(input("Nhập giá trị mới: "))
    ds[ds.index(x)] = new_value
    print("Danh sách sau khi sửa:", ds)
#c
y = int(input("Nhập giá trị cần thêm: "))
vitri = input("Nhập vị trí (dau/cuoi/giua): ")
if vitri == "dau":
    ds.insert(0, y)
elif vitri == "cuoi":
    ds.append(y)
elif vitri == "giua":
    pos = int(input("Nhập vị trí chèn: "))
    ds.insert(pos, y)
print("Danh sách sau khi thêm:", ds)
#d
ds_copy = ds.copy()
for i in range(len(ds_copy)):
    for j in range(i + 1, len(ds_copy)):
        if ds_copy[i] < ds_copy[j]:
            ds_copy[i], ds_copy[j] = ds_copy[j], ds_copy[i]
print("Trước sắp xếp:", ds)
print("Sau sắp xếp giảm dần:", ds_copy)
#e
xoa = int(input("Nhập giá trị cần xóa: "))
print("Trước khi xóa:", ds)
if xoa in ds:
    ds.remove(xoa)
    print("Sau khi xóa:", ds)
else:
    print("Không tồn tại phần tử cần xóa")