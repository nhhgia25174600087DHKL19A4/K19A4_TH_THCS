# hình tròn
def hinh_tron(r):
    if r <= 0:
        return "Bán kính không hợp lệ"

    pi = 3.14
    chu_vi = 2 * pi * r
    dien_tich = pi * r * r

    return chu_vi, dien_tich
# hình vuông
def hinh_vuong(a):
    if a <= 0:
        return "Cạnh không hợp lệ"

    chu_vi = 4 * a
    dien_tich = a * a

    return chu_vi, dien_tich
# hình chữ nhật
def hinh_chu_nhat(dai, rong):
    if dai <= 0 or rong <= 0:
        return "Kích thước không hợp lệ"

    chu_vi = 2 * (dai + rong)
    dien_tich = dai * rong

    return chu_vi, dien_tich
# hình tam giác
def hinh_tam_giac(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Cạnh không hợp lệ"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Không phải tam giác"

    chu_vi = a + b + c
    p = chu_vi / 2

    dien_tich = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    return chu_vi, dien_tich

def main():
    print("1. Hình tròn")
    print("2. Hình vuông")
    print("3. Hình chữ nhật")
    print("4. Hình tam giác")

    chon = int(input("Chọn hình: "))

    if chon == 1:
        r = float(input("Nhập bán kính: "))
        print(hinh_tron(r))

    elif chon == 2:
        a = float(input("Nhập cạnh: "))
        print(hinh_vuong(a))

    elif chon == 3:
        d = float(input("Nhập chiều dài: "))
        r = float(input("Nhập chiều rộng: "))
        print(hinh_chu_nhat(d, r))

    elif chon == 4:
        a = float(input("Nhập cạnh a: "))
        b = float(input("Nhập cạnh b: "))
        c = float(input("Nhập cạnh c: "))
        print(hinh_tam_giac(a, b, c))

    else:
        print("Lựa chọn không hợp lệ")

main()