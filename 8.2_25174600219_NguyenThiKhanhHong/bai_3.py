import random
def la_nt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def tao_ds():
    n = int(input("Nhập n: "))
    ds = []
    for i in range(n):
        x = random.randint(1, 50)
        ds.append(x)
    print("Danh sách:", ds)
    print("Các số nguyên tố:")
    for x in ds:
        if la_nt(x):
            print(x, end=" ")
tao_ds()