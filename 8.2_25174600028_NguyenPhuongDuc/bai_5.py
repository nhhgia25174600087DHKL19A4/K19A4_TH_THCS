import random

def bai_5_kiem_tra_chan_le():
    print("=== BÀI 5 ===")
    n = int(input("Nhập độ dài danh sách n: "))
    danh_sach = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách ban đầu:", danh_sach)
    kiem_tra_chan = lambda x: True if x % 2 == 0 else False
    
    ds_ket_qua = [kiem_tra_chan(i) for i in danh_sach]
    print("Kết quả kiểm tra chẵn (True) / lẻ (False):", ds_ket_qua)
    print("=" * 20)
bai_5_kiem_tra_chan_le()