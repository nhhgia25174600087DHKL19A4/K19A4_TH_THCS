while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    else:
        print("Nhập lại")
ds = list(range(m, n + 1))
chan = list(filter(lambda x: x % 2 == 0, ds))
print("Danh sách ban đầu là :", ds)
print("Số chẵn:", chan)