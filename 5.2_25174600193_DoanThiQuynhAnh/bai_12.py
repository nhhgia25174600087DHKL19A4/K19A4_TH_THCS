username = input("Nhap ten nguoi dung: ")
password = input("Nhap mat khau: ")

ok = True

if len(password) < 6 or len(password) > 12:
    ok = False

if not any(c.islower() for c in password):
    ok = False

if not any(c.isupper() for c in password):
    ok = False

if not any(c.isdigit() for c in password):
    ok = False

if not any(c in "$#@" for c in password):
    ok = False

if ok:
    print("Mat khau hop le")
else:
    print("Mat khau khong hop le")