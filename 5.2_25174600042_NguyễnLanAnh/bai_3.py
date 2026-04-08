a = []
while True:
    n = int(input("Nhập số: "))
    if n == 0:
        break
    a.append(n)
#a
duong = []
con_lai = []
for x in a:
    if x > 0:
        duong.append(x)
    else:
        con_lai.append(x)
a = duong + con_lai
print("Danh sách sau khi chuyển số dương lên đầu:", a)
#b
m = int(input("Nhập số m cần chèn: "))
# Chèn đầu
a.insert(0, m)
a.append(m)
if len(a) >= 5:
    a.insert(4, m)
else:
    a.append(m)
print("Danh sách sau khi chèn m:", a)