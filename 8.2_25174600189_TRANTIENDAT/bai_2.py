import random

def tao_ds_binh_phuong():
    n = int(input("Nhập n: "))
    
    ds = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách:", ds)
    
    binh_phuong = list(map(lambda x: x*x, ds))
    print("Bình phương:", binh_phuong)

tao_ds_binh_phuong()