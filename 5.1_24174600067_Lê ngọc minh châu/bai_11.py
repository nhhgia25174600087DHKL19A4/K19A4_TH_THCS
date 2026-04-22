n = int(input("Nhap n: "))

test_list = []
i = 0
while i < n:
    print("Nhap tuple thu", i)
    so1 = int(input("Nhap so thu 1: "))
    so2 = int(input("Nhap so thu 2: "))
    test_list = test_list + [(so1, so2)]
    i = i + 1

search_tup = []
i = 0
while i < n:
    print("Nhap tuple tim kiem thu", i)
    so1 = int(input("Nhap so thu 1: "))
    so2 = int(input("Nhap so thu 2: "))
    search_tup = search_tup + [(so1, so2)]
    i = i + 1
print("Danh sach kiem tra:", test_list)
print("Danh sach tim kiem:", search_tup)

i = 0
while i < len(search_tup):
    j = 0
    tim = False
    
    while j < len(test_list):
        if search_tup[i] == test_list[j]:
            print("Tuple", search_tup[i], "o vi tri", j)
            tim = True
            break
        j = j + 1
    if tim == False:
        print("Tuple", search_tup[i], "khong co trong danh sach")
    i = i + 1