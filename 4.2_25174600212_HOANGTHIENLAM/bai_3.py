while True:
    x = float(input("Nhập số: ")) 
    if x < 0 or x != int(x): 
        print("Kết thúc!")
        break   
    print("Số hợp lệ:", int(x))