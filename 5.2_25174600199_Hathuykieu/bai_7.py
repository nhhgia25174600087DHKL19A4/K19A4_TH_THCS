#a.
List_ = [["mon", 73], ["tue", 89], ["wed", 95],
         ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
for x in List_:
    print(x)
#b.
print("b)", List_[2][1])
#c.
if len(List_) > 0:
    List_.append(["new", 100])

print("c)", List_)
#d.
tong = 0
for i in [1, 2, 5, 6]:
    tong += List_[i][1]
print("d) Tổng =", tong)