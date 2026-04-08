# 1.
danh_sach = []
while True:
    dong = input("Nhập tên, tuổi, điểm: ")
    if not dong:
        break
    thong_tin = dong.split(",")
    ten = thong_tin[0].strip()
    tuoi = int(thong_tin[1].strip())
    diem = int(thong_tin[2].strip())
    danh_sach.append((ten, tuoi, diem))
# 2.
n = len(danh_sach)
for i in range(n):
    for j in range(0, n - i - 1):
        if danh_sach[j] > danh_sach[j+1]:
            danh_sach[j], danh_sach[j+1] = danh_sach[j+1], danh_sach[j]
print("Danh sách sau khi sắp xếp:")
for item in danh_sach:
    print(item)