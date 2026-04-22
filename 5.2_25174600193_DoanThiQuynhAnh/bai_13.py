passwords = input("Nhap cac mat khau (cach nhau boi dau phay): ").split(",")

ketqua = []

for password in passwords:
    password = password.strip()

    if (6 <= len(password) <= 12 and
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in "$#@" for c in password)):
        ketqua.append(password)

print(",".join(ketqua))