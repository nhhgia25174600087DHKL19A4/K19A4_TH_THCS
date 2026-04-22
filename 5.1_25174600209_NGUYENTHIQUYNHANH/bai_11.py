def nhap_danh_sach(ten_ds, n):
    ds = []
    print(f"\nNhập dữ liệu cho {ten_ds}:")
    for i in range(n):
        print(f"Nhập cặp thứ {i+1}:")
        a = int(input("  Số thứ nhất: "))
        b = int(input("  Số thứ hai: "))
        ds.append((a, b)) 
    return ds
n = int(input("Nhập số lượng cặp n: "))
test_list = nhap_danh_sach("test_list", n)
search_tup = nhap_danh_sach("search_tup", n)
print("\n--- Kết quả tìm kiếm ---")
for i in range(len(search_tup)):
    cap_dang_tim = search_tup[i]
    if cap_dang_tim in test_list:
        index_trong_test = test_list.index(cap_dang_tim)
        print(f"Cặp {cap_dang_tim} xuất hiện tại chỉ mục {index_trong_test} của test_list")