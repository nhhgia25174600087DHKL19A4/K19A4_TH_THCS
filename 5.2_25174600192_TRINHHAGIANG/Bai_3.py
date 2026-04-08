a = []
x = int(input("Nhập số (0 để dừng): "))

while x != 0:
    a.append(x)
    x = int(input("Nhập số (0 để dừng): "))

# a
ds_duong = []
ds_con_lai = []

for i in range(len(a)):
    if a[i] > 0:
        ds_duong.append(a[i])
    else:
        ds_con_lai.append(a[i])

a_moi = ds_duong + ds_con_lai

print("Danh sách sau khi đưa số dương lên đầu:", a_moi)

# b
m = int(input("Nhập m: "))

a_moi.insert(0, m)
a_moi.append(m)
if len(a_moi) >= 5:
    a_moi.insert(4, m)
else:
    a_moi.append(m)

print("Danh sách sau khi chèn:", a_moi)