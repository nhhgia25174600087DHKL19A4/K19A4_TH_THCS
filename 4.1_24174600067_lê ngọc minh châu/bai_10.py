n = int(input("Nhap n: "))
print("So nguyen to:")
x = 2
while x <= n:
    kt = True
    i = 2
    while i < x:
        if x % i == 0:
            kt = False
            break
        i = i + 1
    if kt == True:
        print(x, end=" ")
    x = x + 1
print("So hoan hao:")
x = 1
while x <= n:
    tong = 0
    i = 1
    while i < x:
        if x % i == 0:
            tong = tong + i
        i = i + 1
    if tong == x:
        print(x, end=" ")
    x = x + 1