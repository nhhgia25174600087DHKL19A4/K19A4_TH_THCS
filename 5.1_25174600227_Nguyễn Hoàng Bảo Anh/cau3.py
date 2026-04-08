def la_so_chan(x):
    if x % 2 == 0:
        return True
    return False

while True:
    m = int(input("Nhập m (m > 0): "))
    n = int(input("Nhập n (n > m): "))
    if 0 < m < n:
        break
    print("Lỗi! Điều kiện 0 < m < n không thỏa mãn. Nhập lại!")

ds_so = list(range(m, n + 1))
so_chan = list(filter(la_so_chan, ds_so))
print("Danh sách số chẵn:", so_chan)