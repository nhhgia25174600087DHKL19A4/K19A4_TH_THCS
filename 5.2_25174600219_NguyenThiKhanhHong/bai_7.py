# a.
a = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("Các phần tử trong List_:")
for item in a:
    print(item)
# b. 
b = a[2][1] 
print(f"Giá trị tại vị trí yêu cầu: {b}")
# c. 
print(f"Độ dài hiện tại: {len(a)}")
a.append(["new_day", 100])
print("List sau khi thêm:", a)
# d.
c = ["mon", "tue", "sat", "sun"]
d = 0
for day, value in a:
    if day in c:
        d += value
print(f"Tổng sale value của 4 ngày yêu cầu: {d}")