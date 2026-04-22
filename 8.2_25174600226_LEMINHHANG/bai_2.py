import random

def danh_sach(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách:", ds)
    binh_phuong = list(map(lambda x: x**2, ds))
    print("Bình phương:", binh_phuong)
n = int(input("Nhập n: "))
danh_sach(n)

