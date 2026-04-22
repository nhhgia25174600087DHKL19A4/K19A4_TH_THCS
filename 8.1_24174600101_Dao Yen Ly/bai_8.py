print("1. Hinh tron")
print("2. Hinh vuong")
print("3. Hinh chu nhat")
print("4. Hinh tam giac")

chon = int(input("Chon: "))

if chon == 1:
    r = float(input("Nhap ban kinh: "))
    print("Chu vi =", 2 * 3.14 * r)
    print("Dien tich =", 3.14 * r * r)

elif chon == 2:
    a = float(input("Nhap canh: "))
    print("Chu vi =", 4 * a)
    print("Dien tich =", a * a)

elif chon == 3:
    a = float(input("Nhap chieu dai: "))
    b = float(input("Nhap chieu rong: "))
    print("Chu vi =", 2 * (a + b))
    print("Dien tich =", a * b)

elif chon == 4:
    a = float(input("Nhap canh a: "))
    b = float(input("Nhap canh b: "))
    c = float(input("Nhap canh c: "))

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    print("Chu vi =", a + b + c)
    print("Dien tich =", s)

else:
    print("Lua chon khong hop le")