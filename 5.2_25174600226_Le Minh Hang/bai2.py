# Nhập dữ liệu
n = int(input("Nhập n: "))
a = []
for i in range(n):
    x = int(input(f"a[{i}] = "))
    a.append(x)

# a. Tìm số lớn thứ hai và vị trí
max1 = -1
max2 = -1

for x in a:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x

# tìm vị trí
pos = -1
for i in range(n):
    if a[i] == max2:
        pos = i
        break

if max2 == -1:
    print("a. Không có số lớn thứ hai")
else:
    print("a. Số lớn thứ hai:", max2, "vị trí:", pos)


# b. Số lượng số dương liên tiếp nhiều nhất
max_count = 0
count = 0

for x in a:
    if x > 0:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print("b. Dãy dương liên tiếp dài nhất:", max_count)


# c. Dãy dương liên tiếp có tổng lớn nhất
max_sum = 0
current_sum = 0
count = 0
max_count = 0

for x in a:
    if x > 0:
        current_sum += x
        count += 1
    else:
        if current_sum > max_sum:
            max_sum = current_sum
            max_count = count
        current_sum = 0
        count = 0

# kiểm tra đoạn cuối
if current_sum > max_sum:
    max_sum = current_sum
    max_count = count

print("c. Tổng lớn nhất:", max_sum)
print("   Số phần tử:", max_count)