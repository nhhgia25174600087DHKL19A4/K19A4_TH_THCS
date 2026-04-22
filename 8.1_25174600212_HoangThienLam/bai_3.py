#A,
'''''
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Nhap n: "))
if la_so_nguyen_to(n):
    print("La so nguyen to")
else:
    print("Khong phai")\
    
'''''
#b
'''''
def so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

n = int(input("Nhap n: "))
if so_hoan_hao(n):
    print("La so hoan hao")
else:
    print("Khong phai")
'''''
#c,
def doi_xung(n):
    return str(n) == str(n)[::-1]

dem = 0
for i in range(1, 1001):
    if doi_xung(i):
        print(f"{i:5}", end="")
        dem += 1
        if dem % 15 == 0:
            print()