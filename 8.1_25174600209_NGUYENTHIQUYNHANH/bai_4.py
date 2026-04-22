#a
def tinh_giaithua(n):
    kq = 1
    for i in range(1, n + 1):
        kq = kq * i
    return kq
n = int(input('Nhập n: '))
if n >= 0:
    print('S({}) = {}'.format(n, tinh_giaithua(n)))
else:
    print('n phải >= 0')
#b
def tinh_tong(n):
    kq = 0
    for i in range(n+1):
        kq += (-1)**(i+1) * i
    return kq
n = int(input('Nhap n: '))
if n >= 0:
    print('S({}) = {}'.format(n, tinh_tong(n)))
else:
    print('n phai >= 0')
#c
def tinh_tong_chu_so():
    n = int(input('Nhập n: '))
    if n < 0:
        print('n phải >= 0')
        return
    tong = 0
    temp = n 
    while temp > 0:
        tong += temp % 10  
        temp //= 10       
    print('S({}) = {}'.format(n, tong))
    return
tinh_tong_chu_so()