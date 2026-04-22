n = 0
while n <= 100:
    n = int(input("nhap so "))
a = n
tong = 0
while a > 0:
    tong += a % 10 
    a //= 10        
print(f"tong cac chu so {n} la: {tong}")