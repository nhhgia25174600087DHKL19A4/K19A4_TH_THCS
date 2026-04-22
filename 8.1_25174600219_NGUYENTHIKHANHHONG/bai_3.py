#a:
def kiem_tra_nguyen_to():
    n = int(input("Nhập số nguyên dương n: "))
    if n < 2:
        print(n, "không phải là số nguyên tố")
        return
    for i in range(2, n):
        if n % i == 0:
            print(n, "không phải là số nguyên tố")
            return
    print(n, "là số nguyên tố")
kiem_tra_nguyen_to()

#b:
def kiem_tra_hoan_hao():
    n = int(input("Nhập số nguyên dương n: "))
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải là số hoàn hảo")
kiem_tra_hoan_hao()

#c:
def la_doi_xung(n):
    temp = n
    dao = 0
    while temp > 0:
        dao = dao * 10 + temp % 10
        temp = temp // 10
    return dao == n
def in_doi_xung():
    dem = 0
    for i in range(1000):
        if la_doi_xung(i):
            print(f"{i:5}", end="") 
            dem += 1
            if dem % 15 == 0:
                print()  
in_doi_xung()