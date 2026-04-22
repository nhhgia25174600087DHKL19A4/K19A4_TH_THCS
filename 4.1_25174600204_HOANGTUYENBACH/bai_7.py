while True:
    print("\nNhập phép toán (+, -, *, /) hoặc 0 để thoát")
    op = input("Chọn: ")
    if op == '0':
        break
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        if b != 0:
            print(a / b)
        else:
            print("Không chia được cho 0")
    else:
        print("Phép toán không hợp lệ")