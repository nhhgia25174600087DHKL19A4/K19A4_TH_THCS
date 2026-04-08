lst = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]
index = (len(lst) * 3 + 7) % len(lst)
print("Danh sách:", lst)
print("Số được chọn:", lst[index])