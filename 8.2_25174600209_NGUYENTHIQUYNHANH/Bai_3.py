import random
def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
def bai_3():
    n = int(input("Nhập n: "))
    danh_sach = [random.randint(1, 100) for i in range(n)]
    print("Danh sách ngẫu nhiên:", danh_sach)
    so_nguyen_to = [x for x in danh_sach if la_so_nguyen_to(x)]
    print("Các số nguyên tố trong mảng:", so_nguyen_to)
bai_3()