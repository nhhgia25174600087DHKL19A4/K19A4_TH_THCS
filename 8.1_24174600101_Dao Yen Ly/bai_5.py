def in_ascii():
    while True:
        ky_tu = input("Nhap ky tu (ESC de thoat): ")

        if ky_tu == "ESC":
            break

        print("Ma ASCII:", ord(ky_tu))


in_ascii()