password = input("Nhập mật khẩu: ")
has_lower = False
has_digit = False
has_upper = False
has_special = False
length = len(password)

for ch in password:
    if 'a' <= ch <= 'z':
        has_lower = True
    elif '0' <= ch <= '9':
        has_digit = True
    elif 'A' <= ch <= 'Z':
        has_upper = True
    elif ch in ['S', '#', '@']:
        has_special = True

if length >= 6 and length <= 12 and has_lower and has_digit and has_upper and has_special:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")