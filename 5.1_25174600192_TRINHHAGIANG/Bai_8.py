ds = []
x = int(input("Nhập số (0 để dừng): "))
while x != 0:
    ds.append(x)
    x = int(input("Nhập số (0 để dừng): "))

# a
tim = int(input("Nhập số cần tìm: "))
for i in range(len(ds)):
    if ds[i] == tim:
        print("Vị trí:", i)
        break
# b
moi = int(input("Nhập giá trị mới: "))
ds[i] = moi
print("Danh sách:", ds)
# c
y = int(input("Nhập số cần thêm: "))
ds.append(y)
print("Danh sách:", ds)
# d
for i in range(len(ds)):
    for j in range(len(ds)):
        if ds[i] > ds[j]:
            ds[i], ds[j] = ds[j], ds[i]
print("Sau sắp xếp:", ds)
# e
ds.pop()
print("Sau khi xóa:", ds)