#a
def kt_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def nhap_so_nguyen_duong():
    while True:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        print("n phải là số nguyên dương")
    return n
n = nhap_so_nguyen_duong()
if kt_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố") 
#b
def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False
def kiem_tra_hoan_hao():
    n = int(input("Nhập số nguyên dương n: "))
    
    if la_so_hoan_hao(n):
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải là số hoàn hảo")
kiem_tra_hoan_hao()
#c
def la_so_doi_xung(n):
    s = str(n)
    return s == s[::-1]
def in_so_doi_xung():
    dem = 0 
    for i in range(1000):
        if la_so_doi_xung(i):
            print(f"{i:5}", end=" ")
            dem += 1
            if dem == 15:
                print()
                dem = 0
in_so_doi_xung()