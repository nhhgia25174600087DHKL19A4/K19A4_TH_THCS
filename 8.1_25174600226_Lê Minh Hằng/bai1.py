def giai_thua(a,n):
    if n == 0:
        return 1
    else:
        return a* giai_thua(a,n-1)
a = int(input("Nhập số a: "))
n = int(input("Nhập số n: "))
print("Kết quả",giai_thua(a,n))
