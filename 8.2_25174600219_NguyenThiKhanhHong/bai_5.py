import random
def tao_ds():
    n = int(input("Nhập n: "))
    ds = []
    for i in range(n):
        ds.append(random.randint(1, 50))
    kiem_tra = lambda x: x % 2 == 0
    print("Danh sách:", ds)
    print("Kết quả (True = chẵn, False = lẻ):")
    for x in ds:
        print(x, "->", kiem_tra(x))
tao_ds()