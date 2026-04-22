def in_ascii():
    while True:
        ch = input("Nhập 1 ký tự (nhập 0 để thoát): ")
        if ch == "0":
            print("Kết thúc!")
            break
        if len(ch) != 1:
            print("Chỉ được nhập 1 ký tự!")
            continue
        print("ASCII của", ch, "là:", ord(ch))
in_ascii()