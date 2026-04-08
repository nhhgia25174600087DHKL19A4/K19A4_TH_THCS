List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]

# a. in tung phan tu
for i in range(len(List_)):
    print(List_[i])

# b. phan tu thu 2, vi tri thu 3
print(List_[2][1])

# c. do dai list
print("do dai:", len(List_))

b = [0] * (len(List_) + 1)

for i in range(len(List_)):
    b[i] = List_[i]

b[len(List_)] = ["abc", 100]

print("sau khi them:")
for i in range(len(b)):
    print(b[i])

# d. tinh tong thu 3,4,7,CN (tue, wed, sat, sun)
tong = 0

for i in [1,2,5,6]:
    tong = tong + List_[i][1]

print("tong:", tong)
