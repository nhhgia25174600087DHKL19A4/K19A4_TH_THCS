n = float(input("Nhập số: "))
while True:
    if n < 0 or n != int(n):
        print("Gặp số âm hoặc số thập phân -> dừng chương trình")
        break
    n = float(input("Nhập số tiếp: "))