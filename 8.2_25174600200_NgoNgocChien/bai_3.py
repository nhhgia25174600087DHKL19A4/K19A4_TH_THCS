import random
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def tao_va_in_nguyen_to():
    n = int(input("Nhập số phần tử n: "))
    ds = []
    for i in range(n):
        x = random.randint(1, 100)
        ds.append(x)
    print("Danh sách ban đầu:", ds)
    print("Các số nguyên tố trong danh sách:")
    for x in ds:
        if la_so_nguyen_to(x):
            print(x, end=" ")
tao_va_in_nguyen_to()