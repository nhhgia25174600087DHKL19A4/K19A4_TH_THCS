n = int(input("Nhap so luong tuple: "))

test_list = []
print("Nhap test_list:")

for i in range(n):
    a = int(input("Phan tu 1: "))
    b = int(input("Phan tu 2: "))
    test_list.append((a, b))

search_tup = []
print("Nhap search_tup:")

for i in range(n):
    a = int(input("Phan tu 1: "))
    b = int(input("Phan tu 2: "))
    search_tup.append((a, b))

print("test_list =", test_list)
print("search_tup =", search_tup)
for x in search_tup:
    tim_thay = False
    for i in range(len(test_list)):
        if x == test_list[i]:
            print(x, "xuat hien tai vi tri", i)
            tim_thay = True
            break

    if tim_thay == False:
        print(x, "khong ton tai trong test_list")