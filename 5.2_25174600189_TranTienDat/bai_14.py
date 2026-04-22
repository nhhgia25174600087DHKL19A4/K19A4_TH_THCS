n = int(input("Nhập số phần tử: "))

danh_sach = []

# nhập dữ liệu
for i in range(n):
    ten = input("Nhập tên: ")
    tuoi = int(input("Nhập tuổi: "))
    diem = int(input("Nhập điểm: "))
    
    danh_sach.append((ten, tuoi, diem))

# sắp xếp (bubble sort)
for i in range(len(danh_sach)):
    for j in range(i+1, len(danh_sach)):
        if danh_sach[i][0] > danh_sach[j][0] or \
           (danh_sach[i][0] == danh_sach[j][0] and danh_sach[i][1] > danh_sach[j][1]) or \
           (danh_sach[i][0] == danh_sach[j][0] and danh_sach[i][1] == danh_sach[j][1] and danh_sach[i][2] > danh_sach[j][2]):
            
            # đổi chỗ
            temp = danh_sach[i]
            danh_sach[i] = danh_sach[j]
            danh_sach[j] = temp

# in kết quả
print("Danh sách sau khi sắp xếp:")
for item in danh_sach:
    print(item)