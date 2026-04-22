# a. Tạo list
List_ = [["mon", 73], ["tue", 89], ["wed", 95],
         ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

print("a. Danh sách:")
for item in List_:
    print(item)

# b. Phần tử thứ 2 của sublist thứ 3
print("b. Giá trị cần lấy:", List_[2][1])

# c. Kiểm tra độ dài và thêm sublist
import random

if len(List_) > 0:
    new_item = ["new", random.randint(50, 150)]
    List_.append(new_item)

print("c. Sau khi thêm:", List_)

# d. Tổng sale các ngày mon, tue, sat, sun
tong = 0
for item in List_:
    if item[0] == "mon" or item[0] == "tue" or item[0] == "sat" or item[0] == "sun":
        tong += item[1]

print("d. Tổng sale:", tong)