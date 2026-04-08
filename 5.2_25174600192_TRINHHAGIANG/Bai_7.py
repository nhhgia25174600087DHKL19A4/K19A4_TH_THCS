Danh_sach = [["mon", 73], ["tue", 89], ["wed", 95],
             ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
#a
print("Danh sách các ngày và giá trị bán hàng:")
for phan_tu in Danh_sach:
    print(phan_tu)

# b
gia_tri = Danh_sach[2][1]
print("\nPhần tử thứ hai của sublist thứ ba là:", gia_tri)

# c
do_dai_truoc = len(Danh_sach)
print("\nĐộ dài hiện tại của danh sách:", do_dai_truoc)

# Thêm mới
Danh_sach.append(["them_ngay", 50])
do_dai_sau = len(Danh_sach)
print("Độ dài sau khi thêm sublist:", do_dai_sau)
print("Danh sách sau khi thêm sublist:", Danh_sach)

# d.
vi_tri = [1, 2, 5, 6]

tong_gia_tri = 0
for i in vi_tri:
    tong_gia_tri += Danh_sach[i][1]

print("\nTổng giá trị bán hàng các ngày thứ hai, thứ ba, thứ bảy và chủ nhật:", tong_gia_tri)