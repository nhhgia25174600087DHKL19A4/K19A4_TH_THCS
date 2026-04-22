import random

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def bai3():
    n = int(input("Nhap so luong phan tu: "))
    ds = []
    for i in range(n):
        x = random.randint(1, 100)
        ds.append(x)
    
    print("Danh sach:", ds)
    print("Cac so nguyen to:")
    for x in ds:
        if la_so_nguyen_to(x):
            print(x, end=" ")
bai3()