import random
def kiem_tra_chan():
    n = int(input("Nhập số phần tử n: "))
    ds = []
    for i in range(n):
        x = random.randint(1, 100)
        ds.append(x)
    print("Danh sách ban đầu:", ds)
    kiem_tra = list(map(lambda x: x % 2 == 0, ds))
    print("Kết quả (True: chẵn, False: lẻ):", kiem_tra)
kiem_tra_chan()