import random

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def in_so_nguyen_to():
    n = int(input("Nhập độ dài n: "))
    ds = []
    for i in range(n):
        ds.append(random.randint(1, 100))
    print("Danh sách đã tạo:", ds)
    
    print("Các số nguyên tố trong mảng là:")
    co_so_nguyen_to = False
    for so in ds:
        if la_so_nguyen_to(so):
            print(so, end=" ")
            co_so_nguyen_to = True
            
    if not co_so_nguyen_to:
        print("Không có số nguyên tố nào.")
    print() 

in_so_nguyen_to()