import random
def kiem_tra_nguyen_to(so):
    if so < 2:
        return False
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            return False
    return True
def tao_va_in_nguyen_to():
    n = int(input("Nhập số lượng phần tử n: "))
    danh_sach = []
    for _ in range(n):
        danh_sach.append(random.randint(1, 100))
    print("Danh sách khởi tạo:", danh_sach)
    print("Các số nguyên tố trong danh sách là:")
    for so in danh_sach:
        if kiem_tra_nguyen_to(so):
            print(so, end=" ")
if __name__ == "__main__":
    tao_va_in_nguyen_to()