import random
def tao_va_kiem_tra_chan():
    n = int(input("Nhập số lượng phần tử n: "))
    danh_sach = []
    for _ in range(n):
        danh_sach.append(random.randint(1, 100))
    print("Danh sách khởi tạo:", danh_sach)
    kiem_tra_chan = lambda x: True if x % 2 == 0 else False
    ket_qua = []
    for so in danh_sach:
        ket_qua.append(kiem_tra_chan(so))
if __name__ == "__main__":
    tao_va_kiem_tra_chan()