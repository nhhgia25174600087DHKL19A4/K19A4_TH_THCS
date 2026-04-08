n = int(input("Nhap so luong tuple n = "))
list = []
tup = []
print("Nhap list:")
for i in range(n):
    print("Nhap tuple ", i)
    so1 = int(input("So thu nhat: "))
    so2 = int(input("So thu hai: "))
    cap_so = (so1, so2)
    list = list + [cap_so]
print("Nhap tup")
for i in range(n):
    print("Nhap tuple", i)
    s1 = int(input("S1: "))
    s2 = int(input("S2: "))
    tup = tup + [(s1, s2)]
print("\nDanh sach kiem tra:", list)
print("Danh sach tim kiem:", tup)
print("\n--- KET QUA ---")
for i in range(len(tup)):
    can_tim = tup[i]
    dem = 0
    for j in range(len(list)):
        if can_tim == list[j]:
            print("=> Tim thay", can_tim, "o vi tri", j)
            dem = dem + 1
    if dem == 0:
        print("=> Khong thay", can_tim, "dau ca!")