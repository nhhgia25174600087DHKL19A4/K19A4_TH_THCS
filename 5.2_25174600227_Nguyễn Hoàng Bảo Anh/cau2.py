n = int(input("Nhập n: "))
a = []
for i in range(n):
    a = a + [int(input(f"Nhập a[{i}]: "))]

# a. 
max1 = -999999999
max2 = -999999999
for x in a:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x
print(f"Số lớn thứ hai là: {max2}")

# b. 
max_consec = 0
count = 0
for x in a:
    if x > 0:
        count = count + 1
        if count > max_consec:
            max_consec = count
    else:
        count = 0
print("Số dương liên tiếp nhiều nhất:", max_consec)

# c. 
max_sum = 0
current_sum = 0
for x in a:
    if x > 0:
        current_sum = current_sum + x
        if current_sum > max_sum:
            max_sum = current_sum
    else:
        current_sum = 0
print("Tổng số dương liên tiếp lớn nhất:", max_sum)