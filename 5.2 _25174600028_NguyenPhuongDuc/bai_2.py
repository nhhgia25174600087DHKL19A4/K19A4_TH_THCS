n = int(input("Nhập số phần tử n: "))
lst = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
unique_lst = sorted(list(set(lst)), reverse=True)
if len(unique_lst) >= 2:
    second_max = unique_lst[1]
    positions = [i for i, x in enumerate(lst) if x == second_max]
    print(f"a. Phần tử lớn thứ 2: {second_max}, Vị trí: {positions}")
else:
    print("a. Không có phần tử lớn thứ 2")
max_len, current_len = 0, 0
max_sum, current_sum = 0, 0
for x in lst:
    if x > 0:
        current_len += 1
        current_sum += x
        max_len = max(max_len, current_len)
        max_sum = max(max_sum, current_sum)
    else:
        current_len = 0
        current_sum = 0
print(f"b. Số lượng số dương liên tiếp nhiều nhất: {max_len}")
print(f"c. Tổng các số dương liên tiếp lớn nhất: {max_sum}")