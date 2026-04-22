import random

def tao_ds_va_kiem_tra():
    n = int(input("Nhập độ dài n: "))
    ds = []
    for i in range(n):
        ds.append(random.randint(1, 100))
    
    print("Danh sách đã tạo:", ds)
    kiem_tra_chan = list(map(lambda x: x % 2 == 0, ds))
    
    print("Kết quả kiểm tra chẵn: ", kiem_tra_chan)

tao_ds_va_kiem_tra()