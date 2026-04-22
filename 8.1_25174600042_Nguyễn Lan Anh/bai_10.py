def uoc_so(n):
    kq = []
    for i in range(1, n+1):
        if n % i == 0:
            kq.append(i)
    return kq
n = int(input("Nhập n: "))
print("Các ước:", uoc_so(n))