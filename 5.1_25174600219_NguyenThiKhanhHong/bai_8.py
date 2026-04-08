x = []
while True:
    a = int(input("Nhập số (0 để dừng): "))
    if a == 0:
        break
    x.append(a)
print("Danh sách ban đầu:", x)
# a. Tìm x
n = int(input("Nhập giá trị cần tìm: "))
if n in x:
    vi_tri = x.index(n)
    print("Vị trí của", n, "là:", vi_tri)
else:
    print("Không tìm thấy")
# b. Sửa giá trị
if n in x:
    moi = int(input("Nhập giá trị mới: "))
    x[vi_tri] = moi
    print("Danh sách sau khi sửa:", x)
# c. Thêm phần tử y
y = int(input("Nhập giá trị cần thêm: "))
vitri = int(input("Nhập vị trí muốn thêm: "))
x.insert(vitri, y)
print("Danh sách sau khi thêm:", x)
# d. Sắp xếp giảm dần 
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if x[i] < x[j]:
            x[i], x[j] = x[j], x[i]
print("Danh sách sau khi sắp xếp giảm dần:", x)
# e. Xóa phần tử bất kỳ
print("Danh sách trước khi xóa:", x)
vt_xoa = int(input("Nhập vị trí cần xóa: "))
if 0 <= vt_xoa < len(x):
    x.pop(vt_xoa)
    print("Danh sách sau khi xóa:", x)
else:
    print("Vị trí không hợp lệ")