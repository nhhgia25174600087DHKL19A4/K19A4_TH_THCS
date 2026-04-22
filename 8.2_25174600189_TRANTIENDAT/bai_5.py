import random

def ds_chan():
    n = int(input("Nhập n: "))
    ds = [random.randint(1, 100) for _ in range(n)]
    
    print("Danh sách:", ds)
    
    kq = list(map(lambda x: True if x % 2 == 0 else False, ds))
    print("Kiểm tra chẵn:", kq)

ds_chan()