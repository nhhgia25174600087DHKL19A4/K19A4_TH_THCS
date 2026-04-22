import random
def tao_danh_sach():
    n = int(input("Nhập số phần tử n: "))
    ds = []
    for i in range(n):
        x = random.randint(1, 100)
        ds.append(x)
    print("Danh sách ban đầu:", ds)
    ds_binh_phuong = list(map(lambda x: x**2, ds))
    print("Danh sách bình phương:", ds_binh_phuong)
tao_danh_sach()