# a) P(n) = 1 × 3 × 5 × ... × (2n + 1)
def tinh_P_n():
    n = int(input("Nhập n (>=0) để tính P(n): "))
    ket_qua = 1
    for i in range(n + 1):
        ket_qua *= (2 * i + 1)
    print(f"P({n}) = {ket_qua}")


# b) S(n) = 1 - 2 + 3 - 4 + ... + (-1)^(n+1) * n
def tinh_S_n_dau_tru():
    n = int(input("Nhập n (>=0) để tính S(n): "))
    ket_qua = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            ket_qua -= i
        else:
            ket_qua += i
    print(f"S({n}) = {ket_qua}")


# c) S(n) = 1 + (1+2) + (1+2+3) + ... + (1+2+...+n)
def tinh_S_n_tong_luy_thua():
    n = int(input("Nhập n để tính S(n): "))
    ket_qua = 0
    for i in range(1, n + 1):
        tong = 0
        for j in range(1, i + 1):
            tong += j
        ket_qua += tong
    print(f"S({n}) = {ket_qua}")


# d) P(x, y) = x^y + ∑_{k=1}^{n}(x + 32y + y^k), với n > 1
def tinh_P_x_y():
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    n = int(input("Nhập n (>1): "))

    # Tính x^y bằng nhân lặp
    luy_thua = 1
    for i in range(y):
        luy_thua *= x

    tong = 0
    for k in range(1, n + 1):
        # y^k bằng nhân lặp
        y_mu_k = 1
        for j in range(k):
            y_mu_k *= y
        tong += (x + 32 * y + y_mu_k)

    ket_qua = luy_thua + tong
    print(f"P(x={x}, y={y}, n={n}) = {ket_qua}")

def main():
    print("Bài 4:")
    tinh_P_n()
    tinh_S_n_dau_tru()
    tinh_S_n_tong_luy_thua()
    tinh_P_x_y()
main()
