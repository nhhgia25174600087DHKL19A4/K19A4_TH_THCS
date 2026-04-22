n = int(input("Nhập n: "))
test_list = [0] * n
for i in range(n):
    a = int(input("Nhập phần tử 1 của tuple: "))
    b = int(input("Nhập phần tử 2 của tuple: "))
    test_list[i] = (a, b)

m = int(input("Nhập số phần tử cần tìm: "))
search_tup = [0] * m

for i in range(m):
    a = int(input("Nhập phần tử 1 của tuple cần tìm: "))
    b = int(input("Nhập phần tử 2 của tuple cần tìm: "))
    search_tup[i] = (a, b)

for i in range(m):
    found = False
    for j in range(n):
        if search_tup[i] == test_list[j]:
            print("Tuple", search_tup[i], "ở vị trí", j)
            found = True
            break
    if not found:
        print("Tuple", search_tup[i], "không có trong test_list")