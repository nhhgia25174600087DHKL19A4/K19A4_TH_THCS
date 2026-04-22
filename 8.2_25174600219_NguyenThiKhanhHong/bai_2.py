import random
def tao_danh_sach():
    n = int(input("Nhập n: "))
    m = []
    for i in range(n):
        x = random.randint(1, 10) 
        m.append(x)
    s= list(map(lambda x: x * x, m))
    print("Danh sách ban đầu:", m)
    print("Danh sách bình phương:", s)
tao_danh_sach()