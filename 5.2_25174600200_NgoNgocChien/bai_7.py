# a. Tạo danh sách
List_ = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
for i in range(len(List_)):
    print(List_[i])
#b
print("Giá trị cần lấy:", List_[2][1])
#c
print("Độ dài danh sách:", len(List_))

List_.append(["new",50])

print("Danh sách sau khi thêm:")
print(List_)
#d
tong = 0
for i in range(len(List_)):
    if List_[i][0] == "mon" or List_[i][0] == "tue" or List_[i][0] == "sat" or List_[i][0] == "sun":
        tong = tong + List_[i][1]
print("Tổng sale:", tong)