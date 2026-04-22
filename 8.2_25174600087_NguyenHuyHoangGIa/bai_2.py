import random
def tao_va_tinh_binh_phuong():
    n = int(input("Nhập số lượng phần tử n: "))
    danh_sach = []
    for _ in range(n):
        danh_sach.append(random.randint(1, 100))   
    print("Danh sách khởi tạo:", danh_sach)
    tinh_binh_phuong = lambda x: x * x
    ds_binh_phuong = []
    for so in danh_sach:
        ds_binh_phuong.append(tinh_binh_phuong(so))
    print("Danh sách bình phương:", ds_binh_phuong)
if __name__ == "__main__":
    tao_va_tinh_binh_phuong()