def kiem_tra_nguyen_to():
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 1:
        print(n, "không phải số nguyên tố.")
        return
    la_nguyen_to = True
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break  
    if la_nguyen_to:
        print(n, "số nguyên tố.")
    else:
        print(n, "không phải số nguyên tố.")
def kiem_tra_hoan_hao():
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 1:
        print(n, "không phải số hoàn hảo.")
        return
    tong_uoc_so = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            tong_uoc_so += i    
    if tong_uoc_so == n:
        print(n, "số hoàn hảo.")
    else:
        print(n, "không phải số hoàn hảo.")
def la_so_doi_xung(n):
    so_ban_dau = n
    so_dao_nguoc = 0
    while n > 0:
        chu_so_cuoi = n % 10
        so_dao_nguoc = (so_dao_nguoc * 10) + chu_so_cuoi
        n = n // 10
    return so_ban_dau == so_dao_nguoc
def in_so_doi_xung_pham_vi_1000():
    print("Các số đối xứng trong phạm vi 1000 là:")
    dem = 0
    for i in range(1, 1000):
        if la_so_doi_xung(i):
            print(f"{i:5}", end="")
            dem += 1
            if dem % 15 == 0:
                print()
    if dem % 15 != 0:
        print()
kiem_tra_nguyen_to()
kiem_tra_hoan_hao()
in_so_doi_xung_pham_vi_1000()