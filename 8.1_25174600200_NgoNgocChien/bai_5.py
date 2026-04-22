import msvcrt  
def in_ascii():
    print("Nhấn phím bất kỳ để xem mã ASCII (nhấn ESC để thoát)")
    while True:
        ky_tu = msvcrt.getch() 
        if ky_tu == b'\x1b':
            print("\nĐã thoát chương trình!")
            break
        ky_tu_str = ky_tu.decode('utf-8')
        print("Ký tự:", ky_tu_str, "- ASCII:", ord(ky_tu_str))
in_ascii()