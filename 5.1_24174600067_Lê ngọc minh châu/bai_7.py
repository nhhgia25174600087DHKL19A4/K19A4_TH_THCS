s = input("Nhap chuoi: ")
s = s.strip()
a = s.split()
kq = ""
for i in range(len(a)):
    kq = kq + a[i]
    if i != len(a)-1:
        kq = kq + " "
print(kq)