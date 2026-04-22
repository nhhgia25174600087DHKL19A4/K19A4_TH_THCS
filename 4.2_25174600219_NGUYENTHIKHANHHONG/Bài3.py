print("Nhập số (Chương trình dừng nếu là số âm hoặc số thập phân):")

while True:
    n = input("Nhập một số: ")
    if "." in n:
        print("Đây là số thập phân. Dừng!")
        break
        
    m = int(n)
    
    # Kiểm tra nếu là số âm
    if m < 0:
        print("Đây là số âm. Dừng!")
        break
    
    print(f"Bạn vừa nhập số: {m}")