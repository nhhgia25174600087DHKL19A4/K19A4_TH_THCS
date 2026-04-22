n = int(input("Nhập số lượng n: "))
for i in range(n):
    x = float(input(f"Nhập số thứ {i+1}: "))
    if x < 0:
        print("Gặp số âm, kết thúc chương trình")
        break