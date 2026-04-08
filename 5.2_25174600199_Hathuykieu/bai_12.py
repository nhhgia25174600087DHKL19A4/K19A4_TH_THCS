password = input("Nhập mật khẩu: ")
if len(password) < 6 or len(password) > 12:
    print("Mật khẩu không hợp lệ")
else:
    has_lower = has_upper = has_digit = has_special = False
    
    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in "$#@":
            has_special = True
    
    if has_lower and has_upper and has_digit and has_special:
        print("Mật khẩu hợp lệ")
    else:
        print("Mật khẩu không hợp lệ")