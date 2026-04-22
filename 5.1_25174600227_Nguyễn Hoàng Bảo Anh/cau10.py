n = int(input("Nhập số lượng phần tử lẻ n: "))
ds_le = []
so_chay = 1
while len(ds_le) < n:
    if so_chay % 2 != 0:
        ds_le = ds_le + [so_chay]
    so_chay = so_chay + 1

print("Tuple các số lẻ:", tuple(ds_le))