#a
def ucln(a, b):
    while b != 0:
        a = b
        b = a % b
    return a
#b
def bcnn(a, b):
    return a * b // ucln(a, b)
#c
def rut_gon_phan_so():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    if mau == 0:
        print("Mẫu số phải khác 0")
        return
    UCLN = ucln(tu, mau)
    print("Phân số sau khi rút gọn:", tu // ucln, "/", mau // ucln)
#d
def tim_min_max(a):
    min = a[0]
    max = a[0]
    for x in a:
        if x < min:
            min = x
        if x > max:
            max = x
    return min, max

while True:
    print("1. UCLN")
    print("2. BCNN")
    print("3. Rút gọn phân số")
    print("4. Min - Max")
    print("0. Thoát")

    chon = int(input("Chọn: "))

    if chon == 1:
        a = int(input("a = "))
        b = int(input("b = "))
        print("UCLN:", ucln(a, b))

    elif chon == 2:
        a = int(input("a = "))
        b = int(input("b = "))
        print("BCNN:", bcnn(a, b))

    elif chon == 3:
        tu = int(input("Tử: "))
        mau = int(input("Mẫu: "))
        t, m = rut_gon_phan_so(tu, mau)
        print("Kết quả:", t, "/", m)

    elif chon == 4:
        n = int(input("Nhập n: "))
        a = []
        for i in range(n):
            x = int(input("Nhập số: "))
            a.append(x)

        mn, mx = tim_min_max(a)
        print("Min:", mn)
        print("Max:", mx)

    elif chon == 0:
        print("Thoát chương trình")
        break

    else:
        print("Chọn sai, nhập lại")