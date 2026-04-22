# Hàm cộng, trừ, nhân, chia
def phep_tinh_co_ban():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))

    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Không thể chia cho 0")

# Hàm tính lũy thừa 
def luy_thua(co_so, so_mu):
    kq = 1
    for i in range(so_mu):
        kq *= co_so
    return kq
def tinh_luy_thua_dac_biet():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    n = int(input("Nhập n: "))
    n1 = int(input("Nhập n1: "))

    kq1 = luy_thua(a, b + n1)       # a^(b+n1)
    kq2 = luy_thua(b, n + 2 * a)    # b^(n+2a)

    print(f"a^(b+n1) = {kq1}")
    print(f"b^(n+2a) = {kq2}")

def main():
    print("Bài 9:")
    phep_tinh_co_ban()
    tinh_luy_thua_dac_biet()

main()
