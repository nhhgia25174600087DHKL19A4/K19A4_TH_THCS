def tinh():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    
    print("Tổng: ", a + b)
    print("Hiệu: ", a - b)
    print("Tích: ", a * b)
    
    if b != 0:
        print("Thương: ", a / b)
    else:
        print("Thương: Không thể chia cho 0.")

    n = int(input("Nhập số mũ n: "))
    ket_qua_luy_thua = a ** n
    print("Kết quả", a, "lũy thừa", n, "là:", ket_qua_luy_thua)

tinh()