n = int(input("Nhap tu ban phim"))
temp_list = []
for i in range(n):
    so = int(input("Nhap so thu " + str(i+1) + ": "))
    temp_list.append(so)
tup_goc = tuple(temp_list)
print("Tuple vua nhap:", tup_goc)
le_list = []
for x in tup_goc:
    if x % 2 != 0:
        le_list.append(x)
tup_le = tuple(le_list)
print("Tuple toan so le la:", tup_le)