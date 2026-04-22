a = []
while True:
    v = int(input("Nhập số (0 để dừng): "))
    if v == 0:
        break
    a = a + [v]

# a. 
con_lai = []
for x in a:
    if x > 0:
        duong = duong + [x]
    else:
        con_lai = con_lai + [x]
a = duong + con_lai
print("Danh sách sau khi chuyển dương lên đầu:", a)

# b. 
m = int(input("Nhập m cần chèn: "))

a = [m] + a

a = a + [m]

if len(a) >= 4:
    a = a[:4] + [m] + a[4:]
else:
    a = a + [m]
print("Danh sách sau khi chèn m:", a)