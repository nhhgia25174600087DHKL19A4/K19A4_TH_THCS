s = input("Nhap chuoi: ")
while len(s) > 0 and s[0] == " ":
    s = s[1:]
while len(s) > 0 and s[-1] == " ":
    s = s[:-1]
kq = ""
i = 0
while i < len(s):
    if s[i] != " ":
        kq = kq + s[i]
    else:
        if kq != "" and kq[-1] != " ":
            kq = kq + " "
    i += 1
print("Chuoi chuan hoa:", kq)