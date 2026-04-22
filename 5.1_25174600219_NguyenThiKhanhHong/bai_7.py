s = input("Nhập chuỗi: ")
s = s.strip()  
x = s.split()  
kq = ""
for i in x:
    kq = kq + i + " "
print(kq.strip())