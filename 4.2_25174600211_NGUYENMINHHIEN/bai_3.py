print("Nhập số bất kỳ (dừng nếu là số âm hoặc số thập phân):")
while True:
    txt = input("Nhập số: ")
    if "." in txt:
        print("Dừng do nhập số thập phân.")
        break
    num = int(txt)
    if num < 0:
        print("Dừng do nhập số âm.")
        break