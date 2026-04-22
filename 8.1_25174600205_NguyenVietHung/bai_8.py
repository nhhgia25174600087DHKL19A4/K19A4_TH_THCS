# Hình tròn
def hinh_tron():
    r = float(input("Nhập bán kính: "))

    if r > 0:
        cv = 2 * 3.14 * r
        dt = 3.14 * r * r
        print("Chu vi =", cv)
        print("Diện tích =", dt)
    else:
        print("Bán kính không hợp lệ")

# Hình vuông
def hinh_vuong():
    a = float(input("Nhập cạnh: "))

    if a > 0:
        cv = a * 4
        dt = a * a
        print("Chu vi =", cv)
        print("Diện tích =", dt)
    else:
        print("Cạnh không hợp lệ")

# Hình chữ nhật
def hinh_chu_nhat():
    d = float(input("Nhập chiều dài: "))
    r = float(input("Nhập chiều rộng: "))

    if d > 0 and r > 0:
        cv = (d + r) * 2
        dt = d * r
        print("Chu vi =", cv)
        print("Diện tích =", dt)
    else:
        print("Kích thước không hợp lệ")

# Hình tam giác
def hinh_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        cv = a + b + c
        p = cv / 2
        dt = (p * (p - a) * (p - b) * (p - c)) ** 0.5

        print("Chu vi =", cv)
        print("Diện tích =", dt)
    else:
        print("Ba cạnh không tạo thành tam giác")


print("1. Hình tròn")
print("2. Hình vuông")
print("3. Hình chữ nhật")
print("4. Hình tam giác")

chon = int(input("Chọn hình: "))

if chon == 1:
    hinh_tron()
elif chon == 2:
    hinh_vuong()
elif chon == 3:
    hinh_chu_nhat()
elif chon == 4:
    hinh_tam_giac()
else:
    print("Chọn sai")