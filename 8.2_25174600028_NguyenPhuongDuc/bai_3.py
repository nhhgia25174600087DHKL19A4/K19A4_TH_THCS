import random

def kiem_tra_nguyen_to(so):
    if so < 2:
        return False
    gioi_han = int(so ** 0.5) + 1
    for i in range(2, gioi_han):
        if so % i == 0:
            return False
    return True

def so_nguyen_to():
    print("=== BÀI 3 ===")
    n = int(input("Nhập độ dài danh sách n: "))
    danh_sach = [random.randint(1, 50) for _ in range(n)]
    print("Danh sách ban đầu:", danh_sach)
    ds_nguyen_to = [x for x in danh_sach if kiem_tra_nguyen_to(x)]
    print("Các số nguyên tố có trong danh sách:", ds_nguyen_to)
    print()
so_nguyen_to()