n = int(input("Nhập số lượng phần tử n: "))
danh_sach_tam = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach_tam.append(so)

tuple_cho_truoc = tuple(danh_sach_tam)
danh_sach_le = []
for x in tuple_cho_truoc:
    if x > 0 and x % 2 != 0:
        danh_sach_le.append(x)
tuple_le = tuple(danh_sach_le)
print("Tuple chứa các số lẻ dương là:", tuple_le)