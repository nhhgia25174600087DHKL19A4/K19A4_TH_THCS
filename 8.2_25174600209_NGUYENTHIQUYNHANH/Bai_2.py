import random

def bai_2():
    n = int(input("Nhập độ dài danh sách n: "))
    danh_sach = [random.randint(1, 100) for i in range(n)]
    print("Danh sách gốc:", danh_sach)
    binh_phuong = list(map(lambda x: x**2, danh_sach))
    print("Danh sách bình phương:", binh_phuong)
bai_2()