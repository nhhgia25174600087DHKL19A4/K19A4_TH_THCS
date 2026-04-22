n = int(input("Nhập số phần tử: "))

test_list = []
print("Nhập test_list:")
for i in range(n):
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    test_list.append((a, b))

search_tup = []
print("Nhập search_tup:")
for i in range(n):
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    search_tup.append((a, b))

for x in search_tup:
    found = False
    for i in range(len(test_list)):
        if test_list[i] == x:
            print(x, "xuất hiện tại vị trí:", i)
            found = True
            break
    if not found:
        print(x, "không xuất hiện")