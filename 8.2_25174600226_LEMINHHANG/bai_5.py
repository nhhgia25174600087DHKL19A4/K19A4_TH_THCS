import random
def danh_sach(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách:", ds)
    ket_qua = list(map(lambda x: x % 2 == 0, ds))
    print("Số chẵn (True/False):", ket_qua)
n = int(input("Nhập n: "))
danh_sach(n)