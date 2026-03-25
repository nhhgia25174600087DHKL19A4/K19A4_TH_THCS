n = int(input("Nhap n: "))
if n < 2:
    print("Khong phai so nguyen tp")
else:
    kt = True
    i = 2
    while i < n:
        if n % i == 0:
            kt = False
            break
        i = i + 1
    if kt == True:
        print("La so nguyen to")
    else:
        print("Khong phai so nguyen to")