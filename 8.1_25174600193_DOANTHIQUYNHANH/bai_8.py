def can_bac_hai(x, epsilon=1e-10):
    if x < 0:
        return None
    if x == 0:
        return 0
    guess = x / 2
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2
    return guess

def hinh_tron():
    print("\n--- HÌNH TRÒN ---")
    r = float(input("Nhập bán kính: "))
    if r <= 0:
        print("Bán kính phải lớn hơn 0")
        return
    
    pi = 3.141592653589793
    chu_vi = 2 * pi * r
    dien_tich = pi * r * r
    
    print(f"Chu vi hình tròn: {chu_vi:.2f}")
    print(f"Diện tích hình tròn: {dien_tich:.2f}")

def hinh_vuong():
    print("\n--- HÌNH VUÔNG ---")
    canh = float(input("Nhập độ dài cạnh: "))
    if canh <= 0:
        print("Độ dài cạnh phải lớn hơn 0")
        return
    
    chu_vi = 4 * canh
    dien_tich = canh * canh
    
    print(f"Chu vi hình vuông: {chu_vi:.2f}")
    print(f"Diện tích hình vuông: {dien_tich:.2f}")

def hinh_chu_nhat():
    print("\n--- HÌNH CHỮ NHẬT ---")
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    
    if dai <= 0 or rong <= 0:
        print("Chiều dài và chiều rộng phải lớn hơn 0")
        return
    
    chu_vi = 2 * (dai + rong)
    dien_tich = dai * rong
    
    print(f"Chu vi hình chữ nhật: {chu_vi:.2f}")
    print(f"Diện tích hình chữ nhật: {dien_tich:.2f}")

def hinh_tam_giac():
    print("\n--- HÌNH TAM GIÁC ---")
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))
    
    if a <= 0 or b <= 0 or c <= 0:
        print("Độ dài các cạnh phải lớn hơn 0")
        return
    
    if a + b > c and a + c > b and b + c > a:
        chu_vi = a + b + c
        p = chu_vi / 2
        dien_tich = can_bac_hai(p * (p - a) * (p - b) * (p - c))
        
        print(f"Chu vi hình tam giác: {chu_vi:.2f}")
        print(f"Diện tích hình tam giác: {dien_tich:.2f}")
    else:
        print("Ba cạnh đã nhập KHÔNG tạo thành một tam giác hợp lệ")

def bai_8():
    while True:
        print("\n" + "="*50)
        print("CHƯƠNG TRÌNH TÍNH CHU VI VÀ DIỆN TÍCH CÁC HÌNH")
        print("="*50)
        print("1. Hình tròn")
        print("2. Hình vuông")
        print("3. Hình chữ nhật")
        print("4. Hình tam giác")
        print("0. Thoát")
        print("-"*50)
        
        chon = input("Nhập lựa chọn của bạn (0-4): ")
        
        if chon == "1":
            hinh_tron()
        elif chon == "2":
            hinh_vuong()
        elif chon == "3":
            hinh_chu_nhat()
        elif chon == "4":
            hinh_tam_giac()
        elif chon == "0":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
if __name__ == "__main__":
    bai_8()