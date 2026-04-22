def hinh_tron():
    r = float(input("Nhap ban kinh: "))
    
    if r <= 0:
        print("Ban kinh khong hop le")
        return
    
    pi = 3.14
    chu_vi = 2 * pi * r
    dien_tich = pi * r * r
    
    print("Chu vi:", chu_vi)
    print("Dien tich:", dien_tich)


def hinh_vuong():
    a = float(input("Nhap canh a: "))
    
    if a <= 0:
        print("Canh khong hop le")
        return
    
    print("Chu vi:", 4 * a)
    print("Dien tich:", a * a)


def hinh_chu_nhat():
    a = float(input("Nhap chieu dai: "))
    b = float(input("Nhap chieu rong: "))
    
    if a <= 0 or b <= 0:
        print("Kich thuoc khong hop le")
        return
    
    print("Chu vi:", 2 * (a + b))
    print("Dien tich:", a * b)


def hinh_tam_giac():
    a = float(input("Nhap canh a: "))
    b = float(input("Nhap canh b: "))
    c = float(input("Nhap canh c: "))
    
    if a <= 0 or b <= 0 or c <= 0:
        print("Canh khong hop le")
        return
    
    if a + b <= c or a + c <= b or b + c <= a:
        print("Khong phai tam giac")
        return
    
    chu_vi = a + b + c
    p = chu_vi / 2
    dien_tich = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    
    print("Chu vi:", chu_vi)
    print("Dien tich:", dien_tich)


def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Hinh tron")
        print("2. Hinh vuong")
        print("3. Hinh chu nhat")
        print("4. Hinh tam giac")
        print("0. Thoat")
        
        chon = input("Chon: ")
        
        if chon == "1":
            hinh_tron()
        elif chon == "2":
            hinh_vuong()
        elif chon == "3":
            hinh_chu_nhat()
        elif chon == "4":
            hinh_tam_giac()
        elif chon == "0":
            print("Ket thuc")
            break
        else:
            print("Lua chon khong hop le")


# Chạy chương trình
menu()