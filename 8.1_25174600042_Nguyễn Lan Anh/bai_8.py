def hinh_tron(r):
    cv = 2 * 3.14 * r
    dt = 3.14 * r * r
    return cv, dt
def hinh_vuong(a):
    return 4*a, a*a
def hcn(a, b):
    return 2*(a+b), a*b
def tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        return a+b+c, s
    else:
        return None, None

print("1. Hình tròn")
print("2. Hình vuông")
print("3. HCN")
print("4. Tam giác")

chon = int(input("Chọn: "))

if chon == 1:
    r = float(input("Bán kính: "))
    cv, dt = hinh_tron(r)
    print("Chu vi:", cv)
    print("Diện tích:", dt)

elif chon == 2:
    a = float(input("Cạnh: "))
    cv, dt = hinh_vuong(a)
    print("Chu vi:", cv)
    print("Diện tích:", dt)

elif chon == 3:
    a = float(input("Dài: "))
    b = float(input("Rộng: "))
    cv, dt = hcn(a, b)
    print("Chu vi:", cv)
    print("Diện tích:", dt)

elif chon == 4:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    cv, dt = tam_giac(a, b, c)
    if cv is None:
        print("Không phải tam giác")
    else:
        print("Chu vi:", cv)
        print("Diện tích:", dt)