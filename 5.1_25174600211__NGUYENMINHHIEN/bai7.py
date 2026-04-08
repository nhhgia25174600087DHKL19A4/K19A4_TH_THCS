s = input("Nhập chuỗi: ")
s = s.strip()
ds = s.split()
kq = ""
for i in range(len(ds)):
    kq = kq + ds[i]
    if i != len(ds) - 1:
        kq = kq + " "
print("Chuỗi sau khi chuẩn hóa:")
print(kq)