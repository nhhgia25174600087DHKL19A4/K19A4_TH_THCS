def a():
    while True:
        n = input("Nhập ký tự (ESC để thoát): ")
        if n == "":
            continue
        n = n[0]  
        if ord(n) == 27:
            print("Kết thúc chương trình")
            break
        m = ord(n)
        print("ASCII của ký tự là:", m)
a()