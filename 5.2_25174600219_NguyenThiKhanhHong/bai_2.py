n = int(input("Nhập n: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i}: ")))
# a. 
x1 = max(a)
x2 = -float('inf')
vi_tri_x2 = -1

for i in range(len(a)):
    if a[i] < x1 and a[i] > x2:
        max_2 = a[i]
        vi_tri_x2 = i

if vi_tri_x2 != -1:
    print(f"Số lớn thứ hai là {x2} tại vị trí {vi_tri_x2}")
else:
    print("Không có số lớn thứ hai")
# b. 
b = 0
c = 0

for x in a:
    if x > 0:
        c += 1
        if c > b:
           b = c
    else:
        c = 0
print(f"Số lượng số dương liên tiếp nhiều nhất: {b}")
# c.
max_sum = -1
count_at_max_sum = 0
current_sum = 0
current_count = 0
for x in a:
    if x > 0:
        current_sum += x
        current_count += 1
        if current_sum > max_sum:
            max_sum = current_sum
            count_at_max_sum = current_count
    else:
        current_sum = 0
        current_count = 0
        
print(f"Số lượng số dương liên tiếp trong dãy có tổng lớn nhất: {count_at_max_sum}")