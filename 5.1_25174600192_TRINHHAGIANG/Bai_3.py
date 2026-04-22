def so_chan(x):
    return x % 2 == 0

while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    
    if 0 < m < n:
        break
    else:
        print("Lỗi.Vui lòng nhập lại.")

ds = list(range(m, n + 1))

ket_qua = list(filter(so_chan, ds))

print("Danh sách ban đầu:", ds)
print("Các số chẵn là:", ket_qua)