s = input("Nhap chuoi: ")

s = s.strip()

tu = s.split()
kq = ""

for i in range(len(tu)):
    kq = kq + tu[i]
    if i != len(tu)-1:
        kq = kq + " "

print("Chuoi chuan hoa:", kq)