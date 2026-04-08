a = []
while True:
    n = int(input("Nhập số: "))
    if n == 0:
        break
    a.append(n)
# a.
duong = []
con_lai = []
for x in a:
    if x > 0:
        duong.append(x)
    else:
        con_lai.append(x)
a = duong + con_lai
print("Danh sách sau khi chuyển số dương lên đầu:", a)
# b.
m = int(input("Nhập số m cần chèn: "))
a.insert(0, m)
a.append(m)
if len(a) >= 5:
    a.insert(4, m)
else:
    print("Danh sách không đủ 5 phần tử để chèn vào vị trí thứ 5")
print("Danh sách sau khi chèn m:", a)