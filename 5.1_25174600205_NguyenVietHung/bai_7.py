s = input("Nhập chuỗi: ")
while len(s) > 0 and s[0] == " ":
    s = s[1:]
while len(s) > 0 and s[len(s)-1] == " ":
    s = s[:len(s)-1]
kq = ""
i = 0
while i < len(s):
    if s[i] != " ":
        kq += s[i]
    else:
        kq += " "
        while i < len(s) and s[i] == " ":
            i += 1
        i -= 1
    i += 1

print("Kết quả:", kq)