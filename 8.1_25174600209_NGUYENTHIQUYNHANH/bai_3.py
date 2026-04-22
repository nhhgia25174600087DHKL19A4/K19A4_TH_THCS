#a
def kt_nguyento(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def nhap_so_nguyenduong():
        while True:
            n = int(input("Nhap so nguyen duong n: "))
            if n > 0:
                break
            print("n phai la so nguyen duong")
        return n
n = nhap_so_nguyenduong()
if kt_nguyento(n):
    print(n, "la so nguyen to")
else:
    print(n, "Khong la so nguyen to")
#b
def kt_so_hoan_hao(n):
    if n <= 1:
        return False
    tong_cac_uoc = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            tong_cac_uoc += i
            if i != n // i:
                tong_cac_uoc += n // i
    return tong_cac_uoc == n
def nhap_so_nguyenduong():
    while True:
        n = int(input("Nhap so nguyenduong n: "))
        if n > 0:
            break
        print("n phai la so nguyen duong")
    return n
n = nhap_so_nguyenduong()
if kt_so_hoan_hao(n):
    print(n, "la so hoan hao")
else:
    print(n, "Khong la so hoan hao")
#c
def is_palindrome(n):
    return str(n) == str(n)[::-1]
print('Cac so doi xung trong pham vi 1000 la:')
count = 0
for i in range(1, 1000):
    if is_palindrome(i):
        print(str(i).rjust(3), end=' ')
        count += 1
        if count % 15 == 0:
            print(" ")