def tinh_luy_thua():
    co_so = int(input("Nhập cơ số (số tự nhiên): "))
    so_mu = int(input("Nhập số mũ (số tự nhiên): "))
    ket_qua = 1
    for _ in range(so_mu):
        ket_qua *= co_so
        
    print("Kết quả:", ket_qua)
tinh_luy_thua()