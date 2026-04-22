import random

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ds_so_nguyen_to():
    n = int(input("Nhập n: "))
    ds = [random.randint(1, 100) for _ in range(n)]
    
    print("Danh sách:", ds)
    print("Số nguyên tố:", end=" ")
    
    for x in ds:
        if la_so_nguyen_to(x):
            print(x, end=" ")

ds_so_nguyen_to()