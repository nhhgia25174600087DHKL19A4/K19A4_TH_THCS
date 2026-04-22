n = int(input("Nhập số lượng phần tử n: "))
danh_sach_tam = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach_tam.append(so)
tup = tuple(danh_sach_tam)
print(f"\nTuple vừa nhập là: {tup}")
dem_snt = 0
for x in tup:
    if x > 1:
        la_snt = True
        for i in range(2, x):
            if x % i == 0:
                la_snt = False 
                break
        if la_snt:
            dem_snt += 1
print(f"Kết quả: Trong Tuple có {dem_snt} số nguyên tố.")