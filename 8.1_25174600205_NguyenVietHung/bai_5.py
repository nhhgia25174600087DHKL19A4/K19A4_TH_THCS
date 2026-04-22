def ma_ascii():
    while True:
        kt = input("Nhập ký tự: ")

        if kt == "":
            continue

        if kt == chr(27):
            break

        print("ASCII =", ord(kt[0]))

ma_ascii()