n = int(input("Nhập số lượng phần tử của Tuple: "))
danh_sach_tam = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach_tam.append(so)
tup = tuple(danh_sach_tam)
k = int(input("\nNhập số nguyên k cần đếm: "))
dem = 0
for x in tup:
    if x == k:
        dem += 1
print(f"\nSố {k} xuất hiện {dem} lần trong Tuple {tup}.")