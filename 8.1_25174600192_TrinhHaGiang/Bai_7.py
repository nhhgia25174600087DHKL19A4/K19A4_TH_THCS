# a) Ước chung lớn nhất (UCLN) của 2 số a, b
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def tim_ucln():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print(f"UCLN({a}, {b}) = {ucln(a, b)}")


# b) Bội chung nhỏ nhất (BCNN) của 2 số a, b
def bcnn(a, b):
    return a * b // ucln(a, b)

def tim_bcnn():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print(f"BCNN({a}, {b}) = {bcnn(a, b)}")


# c) Rút gọn phân số
def rut_gon_phan_so():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    if mau == 0:
        print("Phân số không hợp lệ (mẫu số = 0).")
        return
    u = ucln(tu, mau)
    tu //= u
    mau //= u
    print(f"Phân số rút gọn: {tu}/{mau}")


# d) Nhập vào n số nguyên và in ra số nhỏ nhất, lớn nhất
def tim_min_max():
    n = int(input("Nhập số lượng phần tử n: "))
    arr = []
    for i in range(n):
        x = int(input(f"Nhập số thứ {i+1}: "))
        arr.append(x)
    min_val = arr[0]
    max_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    print(f"Số nhỏ nhất: {min_val}")
    print(f"Số lớn nhất: {max_val}")

def main():
    print("Bài 7:")
    tim_ucln()
    tim_bcnn()
    rut_gon_phan_so()
    tim_min_max()
main()
