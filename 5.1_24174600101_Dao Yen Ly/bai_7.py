s = input("Nhap chuoi: ")

# xoa khoang trang dau
while s != "" and s[0] == " ":
    s = s[1:]

# xoa khoang trang cuoi
while s != "" and s[len(s)-1] == " ":
    s = s[:len(s)-1]

kq = ""
dem = 0

for i in range(len(s)):
    if s[i] == " ":
        dem = dem + 1
        if dem == 1:
            kq = kq + " "
    else:
        kq = kq + s[i]
        dem = 0

print("Ket qua:")
print(kq)
