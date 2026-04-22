def in_ascii():
    while True:
        ky_tu = input("Nhap ky tu: ")
        if ky_tu == chr(27):   # ESC
            break
        print("ASCII:", ord(ky_tu))
in_ascii()