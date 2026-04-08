danh_sach = []
while True:
    line = input("Nhập Name, Age, Score (Nhấn Enter trống để dừng): ")
    if not line:
        break
    parts = line.split(',')
    item = (parts[0].strip(), int(parts[1].strip()), int(parts[2].strip()))
    danh_sach.append(item)

n = len(danh_sach)
for i in range(n):
    for j in range(0, n - i - 1):
        if danh_sach[j][0] > danh_sach[j+1][0]:
            danh_sach[j], danh_sach[j+1] = danh_sach[j+1], danh_sach[j]
        elif danh_sach[j][0] == danh_sach[j+1][0]:
            if danh_sach[j][1] > danh_sach[j+1][1]:
                danh_sach[j], danh_sach[j+1] = danh_sach[j+1], danh_sach[j]
            elif danh_sach[j][1] == danh_sach[j+1][1]:
                if danh_sach[j][2] > danh_sach[j+1][2]:
                    danh_sach[j], danh_sach[j+1] = danh_sach[j+1], danh_sach[j]

print("Danh sách sau khi sắp xếp:")
print(danh_sach)