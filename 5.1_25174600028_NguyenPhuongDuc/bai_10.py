n_tuple = int(input("Nhập số lượng phần tử của tuple ban đầu: "))
temp_lst = []
for i in range(n_tuple):
    val = int(input(f"Nhập phần tử thứ {i+1}: "))
    temp_lst += [val]
tup_goc = tuple(temp_lst)
le_lst = []
for x in tup_goc:
    if x > 0 and x % 2 != 0:
        le_lst += [x]
tup_le = tuple(le_lst)
print("Tuple ban đầu:", tup_goc)
print("Tuple chứa số nguyên dương lẻ:", tup_le)