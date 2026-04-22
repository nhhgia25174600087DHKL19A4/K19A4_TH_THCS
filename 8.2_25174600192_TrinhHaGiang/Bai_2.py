import random

def tao_danh_sach():
    n = int(input("Nhap so luong phan tu: "))
    ds = []
    for i in range(n):
        x = random.randint(1, 100)
        ds.append(x)
    binh_phuong = lambda x: x * x
    ds_bp = []
    for x in ds:
        ds_bp.append(binh_phuong(x))
    
    print("Danh sach ban dau:", ds)
    print("Danh sach binh phuong:", ds_bp)
tao_danh_sach()