List_ = [["mon", 73], ["tue", 89], ["wed", 95],
         ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

# a
for x in List_:
    print(x)

# b
print(List_[2][1])   

# c
print(len(List_))
List_.append(["abc", 50])
print(List_)

# d
tong = 0
for x in List_:
    if x[0] in ["mon", "tue", "sat", "sun"]:
        tong += x[1]

print("Tổng:", tong)