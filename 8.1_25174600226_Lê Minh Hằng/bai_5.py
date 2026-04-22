def ASCII():
    while True:
        n = input("Nhập kí tự (gõ ESC để thoát): ")
        if n.lower() == "esc":
            break
        if len(n) == 1:
            print(ord(n))
        else:
            print("nhập 1 ký tự")
ASCII()
        