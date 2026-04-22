n = int(input("Nhap n: "))

if n < 2:
    print("Khong phai so nguyen to")
else:
    la_snt = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_snt = False
            break

    if la_snt:
        print("La so nguyen to")
    else:
        print("Khong phai so nguyen to")