lst = []
while True:
    val = int(input("Nhập số (nhập 0 để dừng): "))
    if val == 0:
        break
    lst.append(val)
lst = [x for x in lst if x > 0] + [x for x in lst if x < 0]
print(" Chuyển số dương lên đầu:", lst)