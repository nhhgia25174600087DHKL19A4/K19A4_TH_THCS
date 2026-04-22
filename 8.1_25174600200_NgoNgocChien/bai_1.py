def luy_thua():
    a = int(input("Nhập số tự nhiên a: "))
    n = int(input("Nhập số mũ n: "))
    ket_qua = 1  
    for i in range(n):
        ket_qua = ket_qua * a
    print("Kết quả là:", ket_qua)
luy_thua() 