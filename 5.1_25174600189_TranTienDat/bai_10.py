n = int(input("Nhập số phần tử: "))

bo_so = ()

# nhập tuple ban đầu
for i in range(n):
    x = int(input("Nhập phần tử: "))
    bo_so = bo_so + (x,)

# lọc số lẻ dương
bo_so_le_duong = ()

for i in bo_so:
    if i > 0 and i % 2 != 0:
        bo_so_le_duong = bo_so_le_duong + (i,)

print("Tuple ban đầu:", bo_so)
print("Tuple số lẻ dương:", bo_so_le_duong)