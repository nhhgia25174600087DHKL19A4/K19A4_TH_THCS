def ascii_ky_tu():
    while True:
        ch = input("Nhập ký tự (ESC để thoát): ")
        if ch == "ESC":
            break
        if len(ch) == 1:
            print("ASCII:", ord(ch))
        else:
            print("Vui lòng chỉ nhập 1 ký tự")
ascii_ky_tu()