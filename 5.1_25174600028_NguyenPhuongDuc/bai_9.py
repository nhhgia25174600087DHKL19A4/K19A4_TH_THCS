while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    print("Lỗi")
danh_sach = []
for i in range(m, n + 1):
    danh_sach = danh_sach + [i]
tup = tuple(danh_sach)
length = 0
for _ in tup: length += 1
giua = length // 2
tp1 = tup[:giua]
tp2 = tup[giua:]
print("Tuple đầu:", tup)
print("Nửa đầu ", tp1)
print("Nửa sau", tp2)