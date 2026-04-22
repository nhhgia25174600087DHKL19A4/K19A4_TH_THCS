import random

def tao_ds_bp():
    n = int(input("Nhập độ dài n: "))
    ds = []
    for i in range(n):
        ds.append(random.randint(1, 100))
    
    print("Danh sách ban đầu:", ds)
    
    binh_phuong = list(map(lambda x: x**2, ds))
    
    print("Danh sách bình phương:", binh_phuong)

tao_ds_bp()