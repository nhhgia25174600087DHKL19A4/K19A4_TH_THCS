n = int(input("Nhập số lượng tuple: "))
test_list = []
for i in range(n):
    a = int(input("Nhập phần tử 1 của tuple: "))
    b = int(input("Nhập phần tử 2 của tuple: "))
    test_list.append((a, b))

search_tup = []
for i in range(n):
    a = int(input("Nhập phần tử 1 của tuple tìm kiếm: "))
    b = int(input("Nhập phần tử 2 của tuple tìm kiếm: "))
    search_tup.append((a, b))
print("Các tuple xuất hiện trong test_list:")
for t in search_tup:
    if t in test_list:
        print(t)