import random
def bai_5():
    n = int(input("Nhập n: "))
    danh_sach = [random.randint(1, 100) for i in range(n)]
    print("Danh sách ngẫu nhiên:", danh_sach)
    kiem_tra = list(map(lambda x: True if x % 2 == 0 else False, danh_sach))
    print("Kết quả kiểm tra (True=Chẵn, False=Lẻ):", kiem_tra)
bai_5()