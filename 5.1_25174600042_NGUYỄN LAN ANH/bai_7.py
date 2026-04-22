s = input("Nhap chuoi: ")

# xoa dau cuoi
s = s.strip()

# tach thanh cac tu
tu = s.split()

# ghep lai
kq = ""
for i in range(len(tu)):
    kq += tu[i]
    if i != len(tu) - 1:
        kq += " "

print("Chuoi sau khi chuan hoa:", kq)