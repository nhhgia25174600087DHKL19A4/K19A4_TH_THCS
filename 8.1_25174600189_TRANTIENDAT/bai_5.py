def in_ascii():
    while True:
        ky_tu = input("Nhập ký tự: ")
        if ky_tu == "":
            continue

        ma = ord(ky_tu[0])  

        if ma == 27:  
            print("Kết thúc chương trình")
            break

        print("ASCII:", ma)

in_ascii()