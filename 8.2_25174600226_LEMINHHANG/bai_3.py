import random
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def danh_sach(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách:", ds)
    snt = list(filter(lambda x: la_so_nguyen_to(x), ds))
    print("Số nguyên tố:", snt)
n = int(input("Nhập n: "))
danh_sach(n)