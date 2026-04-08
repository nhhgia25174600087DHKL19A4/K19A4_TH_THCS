n = int(input("Nhap so luong cap so muon co: "))
test_list = []
for i in range(n):
    print("Nhap cap thu", i)
    so1 = int(input("   So thu nhat: "))
    so2 = int(input("   So thu hai: "))
    test_list.append((so1, so2))
m = int(input("Nhap so luong cap muon tim: "))
search_tup = []
for i in range(m):
    print("Nhap cap muon tim thu", i)
    a = int(input("   So thu nhat: "))
    b = int(input("   So thu hai: "))
    search_tup.append((a, b))
print("--- KET QUA ---")
for x in search_tup:
    if x in test_list:
        vitri = test_list.index(x)
        print(x, "o vi tri", vitri)
    else:
        print(x, "khong co")