n = int(input("Nhap so luong phan tu trong moi danh sach: "))

test_list = []
search_tup = []

print("Nhap danh sach kiem tra:")
for i in range(n):
    a = int(input("Nhap so thu nhat: "))
    b = int(input("Nhap so thu hai: "))
    test_list.append((a, b))

print("Nhap danh sach tim kiem:")
for i in range(n):
    a = int(input("Nhap so thu nhat: "))
    b = int(input("Nhap so thu hai: "))
    search_tup.append((a, b))

print("Danh sach kiem tra:", test_list)
print("Danh sach tim kiem:", search_tup)

print("Ket qua tim vi tri:")

for i in range(len(search_tup)):
    tim_thay = False
    for j in range(len(test_list)):
        if search_tup[i] == test_list[j]:
            print(search_tup[i], "xuat hien tai vi tri", j)
            tim_thay = True
            break
    if tim_thay == False:
        print(search_tup[i], "khong xuat hien trong danh sach")