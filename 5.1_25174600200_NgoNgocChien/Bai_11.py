n = int(input("Nhap n: "))
test_list = []
search_tup = []
print("Nhap test_list:")
for i in range(n):
    a = int(input("Nhap so thu 1: "))
    b = int(input("Nhap so thu 2: "))
    test_list.append((a, b))
print("Nhap search_tup:")
for i in range(n):
    a = int(input("Nhap so thu 1: "))
    b = int(input("Nhap so thu 2: "))
    search_tup.append((a, b))
print("Ket qua:")
for i in range(len(search_tup)):
    for j in range(len(test_list)):
        if search_tup[i] == test_list[j]:
            print(search_tup[i], "xuat hien tai vi tri", j)