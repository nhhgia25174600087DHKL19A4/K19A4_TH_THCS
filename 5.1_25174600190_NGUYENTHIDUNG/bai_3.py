ktra = False
while not ktra:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    
    if 0 < m < n:
        ktra = True
    else:
        print("Lỗi: Điều kiện 0 < m < n !")

danh_sach_goc = list(range(m, n + 1))
danh_sach_chan = list(filter(lambda x: x % 2 == 0, danh_sach_goc))
print(f"Danh sách từ {m} đến {n}:", danh_sach_goc)
print("Các số chẵn tìm được:", danh_sach_chan)
