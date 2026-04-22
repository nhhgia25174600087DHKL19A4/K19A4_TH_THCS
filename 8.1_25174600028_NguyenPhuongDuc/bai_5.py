def ham_ma_ascii():
    print("nhập một ký tự để xem mã ASCII nhập 'esc' để thoát.")
    while True:
        char = input("Nhập ký tự: ")
        if char.upper() == 'ESC':
            print("end.")
            break
        elif len(char) == 1:
            print(f"mã ASCII của '{char}' là {ord(char)}")
        else:
            print(" chỉ nhập 1 ký tự.")
ham_ma_ascii()