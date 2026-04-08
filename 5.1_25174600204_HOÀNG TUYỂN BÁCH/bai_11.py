
n = int(input("Nhập số lượng tuple cho danh sách kiểm tra (test_list): "))
test_list = []
print("Nhập các tuple cho test_list (2 số tự nhiên mỗi tuple):")
for i in range(n):
    a = int(input(f"Tuple {i+1}, số thứ 1: "))
    b = int(input(f"Tuple {i+1}, số thứ 2: "))
    test_list.append((a, b))

print("Danh sách kiểm tra test_list:", test_list)
m = int(input("Nhập số lượng tuple cho danh sách tìm kiếm (search_tup): "))
search_tup = []
print("Nhập các tuple cho search_tup (2 số tự nhiên mỗi tuple):")
for i in range(m):
    a = int(input(f"Tuple {i+1}, số thứ 1: "))
    b = int(input(f"Tuple {i+1}, số thứ 2: "))
    search_tup.append((a, b))

print("Danh sách tìm kiếm search_tup:", search_tup)
print("\nKết quả tìm kiếm (chỉ số trong search_tup xuất hiện trong test_list):")
for i in range(len(search_tup)):
    if search_tup[i] in test_list:
        print(f"Tuple {search_tup[i]} xuất hiện tại index {i} trong search_tup")