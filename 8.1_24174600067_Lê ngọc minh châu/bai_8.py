# tron
def tron(r):
    if r > 0:
        print("Chu vi:", 2*3.14*r)
        print("Dien tich:", 3.14*r*r)
    else:
        print("Ban kinh khong hop le")

# vuong
def vuong(a):
    if a > 0:
        print("Chu vi:", 4*a)
        print("Dien tich:", a*a)

# chu nhat
def chu_nhat(d, r):
    if d > 0 and r > 0:
        print("Chu vi:", 2*(d+r))
        print("Dien tich:", d*r)

# tam giac
def tam_giac(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        p = (a+b+c)/2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        print("Chu vi:", a+b+c)
        print("Dien tich:", s)
    else:
        print("Khong phai tam giac")

print("Chon hinh:")
print("1. Hinh tron")
print("2. Hinh vuong")
print("3. Hinh chu nhat")
print("4. Hinh tam giac")

chon = int(input("Nhap lua chon: "))
if chon == 1:
    r = float(input("Nhap ban kinh: "))
    tron(r)
elif chon == 2:
    a = float(input("Nhap canh: "))
    vuong(a)
elif chon == 3:
    d = float(input("Nhap dai: "))
    r = float(input("Nhap rong: "))
    chu_nhat(d, r)
elif chon == 4:
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    c = float(input("Nhap c: "))
    tam_giac(a, b, c)
else:
    print("Lua chon sai")