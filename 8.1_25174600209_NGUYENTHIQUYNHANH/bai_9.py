def phep_tinh_co_ban(a, b):
    print("\n--- Kết quả các phép tính cơ bản ---")
    print("{} + {} = {}".format(a, b, a + b))
    print("{} - {} = {}".format(a, b, a - b))
    print("{} * {} = {}".format(a, b, a * b))
    if b != 0:
        print("{} / {} = {}".format(a, b, a / b))
    else:
        print("Không thể thực hiện phép chia cho 0")
def tinh_luy_thua_1(a, b, n):
    kq = a ** (b + n)
    return kq
def tinh_luy_thua_2(a, b, n):
    kq = b ** (n + 2 * a)
    return kq
def bai_9():
    print("--- Chương trình tính toán Bài 9 ---")
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    n = float(input("Nhập số n: "))
    phep_tinh_co_ban(a, b)
    lt1 = tinh_luy_thua_1(a, b, n)
    lt2 = tinh_luy_thua_2(a, b, n)
    print("\n--- Kết quả tính lũy thừa ---")
    print("Giá trị a^(b+n) là: {}".format(lt1))
    print("Giá trị b^(n+2a) là: {}".format(lt2))
bai_9()