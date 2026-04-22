while True:
    ch = input("Nhap ky tu (ESC de thoat): ")
    
    if ch == chr(27):
        break
    
    print("ASCII:", ord(ch))