List_ = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]

# a
print(List_)

# b
print(List_[2][1])

# c
if len(List_) > 0:
    List_.append(["new",100])

# d
tong = List_[0][1] + List_[1][1] + List_[5][1] + List_[6][1]
print("Tổng:", tong)