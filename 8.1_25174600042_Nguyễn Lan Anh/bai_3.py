#a
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập n: "))
if la_so_nguyen_to(n):
    print("Là số nguyên tố")
else:
    print("Không phải số nguyên tố")
#b
def kiem_tra_so_hoan_hao():
    n = int(input("Nhập n để kiểm tra số hoàn hảo: "))
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong = tong + i
    if tong == n and n != 0:
        print("Là số hoàn hảo")
    else:
        print("không phải là số hoàn hảo")
kiem_tra_so_hoan_hao()    
#c
def la_doi_xung(n):
    s = str(n)
    return s == s[::-1]
dem = 0
for i in range(1000):
    if la_doi_xung(i):
        print(f"{i:5}", end="")  
        dem = dem + 1
        if dem % 15 == 0:
            print()