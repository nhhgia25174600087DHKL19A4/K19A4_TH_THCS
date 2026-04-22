# phan a:
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

# phan b:
def kiem_tra_hoan_hao(n):
    tong = 0
    i = 1

    while i < n:
        if n % i == 0:
            tong = tong + i
        i = i + 1

    if tong == n:
        return True
    return False


n = int(input("Nhap n: "))
if kiem_tra_hoan_hao(n):
    print("La so hoan hao")
else:
    print("Khong phai")

# phan c:
def doi_xung(n):
    return str(n) == str(n)[::-1]

count = 0
for i in range(1000):
    if doi_xung(i):
        print(f"{i:05}", end=" ")
        count += 1
        if count % 15 == 0:
            print()