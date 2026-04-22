while True:
 m = int(input("Nhập m (m > 0): "))
 n = int(input("Nhập n (n > m): "))
 if 0 < m < n:
    break
 else:
    print("Lỗi, Nhập lại m và n")
danh_sach_goc = list(range(m, n + 1))
danh_sach_chan = []
for so in danh_sach_goc:
    if so % 2 == 0: 
        danh_sach_chan.append(so)
print(f"Các số chẵn trong đoạn [{m}, {n}] là:", danh_sach_chan)

