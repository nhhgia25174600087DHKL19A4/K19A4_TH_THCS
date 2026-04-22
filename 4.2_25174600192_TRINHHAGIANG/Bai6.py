while True:
    n = int(input("Nhập số (>100): "))
    if n > 100:
        break
    print("Phải nhập số > 100, nhập lại!")

tong = 0
while n > 0:
    tong += n % 10  
    n //= 10         

print("Tổng các chữ số =", tong)