n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

if 0 < m < n:
    danh_sach_goc = list(range(m, n + 1))
    
    def la_so_chan(x):
        return x % 2 == 0
    ket_qua = list(filter(la_so_chan, danh_sach_goc))
    print("Kết quả là: ", ket_qua)
else:
    print("Lỗi: Vui lòng nhập thỏa mãn điều kiện")