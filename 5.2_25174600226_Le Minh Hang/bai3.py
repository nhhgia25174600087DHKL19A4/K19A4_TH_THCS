# Nhập danh sách đến khi gặp 0 thì dừng
a = []
while True:
    x = int(input("Nhập số (0 để dừng): "))
    if x == 0:
        break
    a.append(x)

# a. Đưa số dương lên đầu danh sách
duong = []
khac = []

for x in a:
    if x > 0:
        duong.append(x)
    else:
        khac.append(x)

# ghép lại
a = duong + khac

print("a. Danh sách sau khi đưa số dương lên đầu:")
print(a)


# b. Chèn số m vào các vị trí
m = int(input("Nhập số m: "))

# chèn đầu
a.insert(0, m)

# chèn cuối
a.append(m)

# chèn vị trí thứ 5 (index 4)
if len(a) >= 4:
    a.insert(4, m)
else:
    a.append(m)  # nếu không đủ thì cho vào cuối

print("b. Danh sách sau khi chèn:")
print(a)