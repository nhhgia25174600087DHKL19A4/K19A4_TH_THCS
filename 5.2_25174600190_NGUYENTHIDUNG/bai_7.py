lst = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

# a
for item in lst:
    print(item)

# b
print(lst[1][1])

# c
print("Độ dài:", len(lst))
lst.append(["new_day", 100])

# d
total = 0
for i in [1, 2, 5, 6]:
    total += lst[i][1]

print("Tổng:", total)