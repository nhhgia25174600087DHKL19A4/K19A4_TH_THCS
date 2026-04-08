List_ = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print("a. Các phần tử trong List_:")
for sublist in List_:
    print(sublist)
sublist_thu_hai = List_[1] 
gia_tri_sale = sublist_thu_hai[1] 
print(f"\nb. Phần tử số của sublist thứ hai là: {gia_tri_sale}")
list_test = List_[:] 
print(f"\nc. Độ dài của list hiện tại: {len(list_test)}")
ngay_moi = "special_day"
sale_ngau_nhien = (len(list_test) * 77 + 13) % 150 
list_test = list_test + [[ngay_moi, sale_ngau_nhien]]
print(f"Danh sách sau khi thêm sublist mới: {list_test}")
tong_sale = 0
ngay_can_tinh = ["mon", "tue", "sat", "sun"]
for sublist in List_:
    if sublist[0] in ngay_can_tinh:
        tong_sale += sublist[1]
print(f"\nd. Tổng sale của Mon, Tue, Sat, Sun là: {tong_sale}")