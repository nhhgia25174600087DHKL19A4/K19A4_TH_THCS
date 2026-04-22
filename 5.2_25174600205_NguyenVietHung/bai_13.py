
def check_password(pw):
    has_lower = False
    has_digit = False
    has_upper = False
    has_special = False
    length = len(pw)

    for ch in pw:
        if 'a' <= ch <= 'z':
            has_lower = True
        elif '0' <= ch <= '9':
            has_digit = True
        elif 'A' <= ch <= 'Z':
            has_upper = True
        elif ch in ['S', '#', '@']:
            has_special = True

    if length >= 6 and length <= 12 and has_lower and has_digit and has_upper and has_special:
        return True
    else:
        return False


s = input("Nhập chuỗi mật khẩu, phân cách bằng dấu phẩy: ")

passwords = []
start = 0
for i in range(len(s)):
    if s[i] == ',':
        passwords.append(s[start:i].strip())
        start = i + 1
passwords.append(s[start:].strip())  

for pw in passwords:
    if check_password(pw):
        print(pw, ": hợp lệ")
    else:
        print(pw, ": không hợp lệ")