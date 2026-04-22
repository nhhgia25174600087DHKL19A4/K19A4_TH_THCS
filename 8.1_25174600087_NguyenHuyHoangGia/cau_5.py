def in_ma_ascii():
    print("Chương trình tra cứu mã ASCII")
    while True:
        ky_tu = input("Nhập một ký tự: ")
        if ky_tu == chr(27): 
            print("Đã thoát chương trình.")
            break
        if len(ky_tu) == 1:
            print(f"Mã ASCII của '{ky_tu}' là: {ord(ky_tu)}")
        elif chr(27) in ky_tu:
            print("Đã thoát chương trình.")
            break
        else:
            print("Vui lòng chỉ nhập 1 ký tự")
in_ma_ascii()