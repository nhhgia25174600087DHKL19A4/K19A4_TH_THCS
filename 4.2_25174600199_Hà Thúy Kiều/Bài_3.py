for _ in range(1000000):
    x = float(input("Nhập số: "))
    
    if x < 0 or x != int(x):
        break
print("Đã dừng!")