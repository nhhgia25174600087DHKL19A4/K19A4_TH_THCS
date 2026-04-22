import random

def bai5():
    n = int(input("Nhap so luong phan tu: "))
    ds = []
    for i in range(n):
        x = random.randint(1, 100)
        ds.append(x)
    la_chan = lambda x: x % 2 == 0

    print("Danh sach:", ds)
    print("Ket qua kiem tra chan:")
    for x in ds:
        print(x, "->", la_chan(x))
bai5()