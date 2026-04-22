while True:
    x = float(input("Nhập số: "))

    if x < 0 or x != int(x):
        print("Gặp số âm hoặc số thập phân -> dừng chương trình")
        break