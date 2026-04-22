# Hình tròn
def tron():
    r = float(input("r = "))
    if r > 0:
        print("Chu vi:", 2 * 3.14 * r)
        print("Diện tích:", 3.14 * r * r)
    else:
        print("Sai")

# Hình vuông
def vuong():
    a = float(input("a = "))
    if a > 0:
        print("Chu vi:", 4 * a)
        print("Diện tích:", a * a)
    else:
        print("Sai")

# Hình chữ nhật
def hcn():
    a = float(input("dài = "))
    b = float(input("rộng = "))
    if a > 0 and b > 0:
        print("Chu vi:", 2 * (a + b))
        print("Diện tích:", a * b)
    else:
        print("Sai")

# Hình tam giác
def tamgiac():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if a > 0 and b > 0 and c > 0 and a+b>c and a+c>b and b+c>a:
        p = (a + b + c) / 2
        s = (p*(p-a)*(p-b)*(p-c)) ** 0.5
        print("Chu vi:", a + b + c)
        print("Diện tích:", s)
    else:
        print("Sai")
tron()
vuong()
hcn()
tamgiac()