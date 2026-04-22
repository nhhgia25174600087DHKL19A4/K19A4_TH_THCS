#a
def kiem_tra_nt(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True
n = int(input("Nhap n: "))
if kiem_tra_nt(n):
    print("La so nguyen to")
else:
    print("Khong phai")

#b
def kiem_tra_hh(n):
    tong = 0
    i = 1
    while i < n:
        if n % i == 0:
            tong = tong + i
        i = i + 1
    return tong == n

n = int(input("Nhap n: "))
if kiem_tra_hh(n):
    print("La so hoan hao")
else:
    print("Khong phai")

#c
def doi_xung(n):
    return str(n) == str(n)[::-1]
dem = 0
i = 0
while i < 1000:
    if doi_xung(i):
        print(f"{i:5}", end="")
        dem = dem + 1
        if dem % 15 == 0:
            print()
    i = i + 1