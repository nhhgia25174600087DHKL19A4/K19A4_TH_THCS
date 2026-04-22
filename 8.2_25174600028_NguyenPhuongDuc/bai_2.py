import random

def binh_phuong_lambda():
    print("=== BÀI 2 ===")
    n = int(input("Nhập độ dài danh sách n: "))
    danh_sach = [random.randint(1, 10) for _ in range(n)]
    print("Danh sách ban đầu:", danh_sach)
    tinh_binh_phuong = lambda x: x * x
    ds_binh_phuong = [tinh_binh_phuong(i) for i in danh_sach]
    print("Danh sách sau khi bình phương:", ds_binh_phuong)
    print()
binh_phuong_lambda()