n = int(input("Nhập số lượng phần tử n: "))
danh_sach_tam = []

for i in range(n):
    so = float(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach_tam.append(so)
tup = tuple(danh_sach_tam)
print(f"\nTuple vừa nhập là: {tup}")
tong = 0
for x in tup:
    tong += x
if len(tup) > 0:
    tbc = tong / len(tup)
    print(f"a. Trung bình cộng các phần tử: {tbc}")
else:
    print("a. Tuple trống, không tính được trung bình cộng.")
dem = 0
if len(tup) > 0:
    for x in tup:
        if x > tbc:
            dem += 1
    print(f"b. Số lượng phần tử lớn hơn TBC ({tbc}) là: {dem}")