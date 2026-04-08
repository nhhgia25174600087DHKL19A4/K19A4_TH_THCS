List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103],
         ["fri", 115], ["sat", 128], ["sun", 120]]

for i in List_:
    print(i)

print(List_[2][1])

import random

if len(List_) > 0:
    List_.append(["new", random.randint(50,150)])

print(List_)

tong = 0
for i in List_:
    if i[0] in ["mon", "tue", "sat", "sun"]:
        tong += i[1]

print(tong)
