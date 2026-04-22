def bai5():
    while True:
        ky_tu = input("Nhap 1 ky tu (ESC de thoat): ")
        

        if ky_tu == "":
            continue
        
        # Lấy ký tự đầu tiên
        ky_tu = ky_tu[0]
        
        ma = ord(ky_tu)
        
        # Kiểm tra ESC
        if ma == 27:
            print("Thoat chuong trinh")
            break
        
        print("Ma ASCII cua", ky_tu, "la:", ma)


# Gọi hàm
bai5()