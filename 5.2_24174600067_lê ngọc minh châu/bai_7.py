List_ = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
# a,in list
print(List_)
# b,lay phan tu thu 2 cua sublist thu 3
print(List_[2][1])

# c,them sublist moi
List_ = List_ + [["new",100]]

# d,tinh tong cac ngay mon, tue, sat, sun
tong = 0
for i in range(len(List_)):
    if List_[i][0] == "mon" or List_[i][0] == "tue" or List_[i][0] == "sat" or List_[i][0] == "sun":
        tong = tong + List_[i][1]

print("Tong =", tong)