def in_ascii_den_esc():
    while True:
        ky_tu = input("Nhập một ký tự: ")
        if len(ky_tu) == 1 and ord(ky_tu) == 27:
            break
        print(f"ASCII của '{ky_tu}' là: {ord(ky_tu)}")

in_ascii_den_esc()