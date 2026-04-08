# a
List_ = [["mon", 73], ["tue", 89], ["wed", 95],
         ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

print("Danh sách:")
for i in range(len(List_)):
    print(List_[i])

# b
# sublist thứ 3 -> index = 2
# phần tử thứ 2 -> index = 1
x = List_[2][1]
print("Phần tử cần lấy:", x)

# c
print("Độ dài list:", len(List_))

List_.append(["new_day", 150])

print("Sau khi thêm:")
for i in range(len(List_)):
    print(List_[i])

# d
tong = 0

for i in range(len(List_)):
    if List_[i][0] == "mon" or List_[i][0] == "tue" \
       or List_[i][0] == "sat" or List_[i][0] == "sun":
        tong = tong + List_[i][1]

print("Tổng sale (mon, tue, sat, sun):", tong)