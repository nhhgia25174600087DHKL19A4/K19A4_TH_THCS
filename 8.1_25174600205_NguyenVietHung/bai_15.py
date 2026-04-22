# a) 
def cau_a():
    ds = []

    for i in range(1, 101):
        if i % 2 == 0:
            ds = ds + [i]

    print("List số chẵn:", ds)


# Hàm reduce tự tạo
def cong_tong(ds):
    tong = 0
    for x in ds:
        tong = tong + x
    return tong

# b) 
def cau_b():
    n = int(input("Nhập n: "))

    ds = []
    for i in range(1, n + 1):
        ds = ds + [i]

    chan = list(filter(lambda x: x % 2 == 0, ds))

    tong = cong_tong(chan)

    print("Danh sách:", ds)
    print("Các số chẵn:", chan)
    print("Tổng số chẵn =", tong)

cau_a()
cau_b()