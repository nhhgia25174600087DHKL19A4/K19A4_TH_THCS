a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
x, y = a, b
while x != y:
    if x > y:
        x = x - y
    else:
        y = y - x
ucln = x
for i in range(1):
    bcnn = (a * b) // ucln
    print("BCNN:", bcnn)