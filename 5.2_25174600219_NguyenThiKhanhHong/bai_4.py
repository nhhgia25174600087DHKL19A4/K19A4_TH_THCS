ds = []
while True:
    v = int(input("Nhập phần tử cho bài 4 (0 để dừng): "))
    if v == 0: break
    ds.append(v)
# a.
a = [1, 2, 3]
ds = a + ds + a
if len(ds) >= 5:
    ds[4:4] = a
print("Danh sách sau khi chèn [1,2,3]:", ds)
# b.
k = int(input("Nhập vị trí k cần xóa: "))
if 0 <= k < len(ds):
    ds.pop(k)
    print(f"Danh sách sau khi xóa vị trí {k}:", ds)
# c.
ds.sort()
print("Tăng dần:", ds)
ds.sort(reverse=True)
print("Giảm dần:", ds)