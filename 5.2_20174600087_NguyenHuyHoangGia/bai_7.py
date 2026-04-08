# a.
List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
for item in List_:
    print(item)
# b.
ket_qua_b = List_[2][1]
print(f"Phần tử thứ hai của sublist thứ 3 là: {ket_qua_b}")
# c.
print("Độ dài của list hiện tại:", len(List_))
new_sublist = ["test", 999]
List_.append(new_sublist)
print("Danh sách sau khi thêm sublist mới:", List_)
# d.
tong_sale = 0
for ngay in List_:
    ten_ngay = ngay[0]
    gia_tri = ngay[1]
    if ten_ngay == "mon" or ten_ngay == "tue" or ten_ngay == "sat" or ten_ngay == "sun":
        tong_sale += gia_tri
print("Tổng sale value của Mon, Tue, Sat, Sun là:", tong_sale)