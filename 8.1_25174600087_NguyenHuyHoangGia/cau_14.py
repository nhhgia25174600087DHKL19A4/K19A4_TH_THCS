def xu_ly_list_voi_map_lambda():
    n = int(input("Nhập số lượng phần tử n cho list: "))
    list_goc = []
    for i in range(n):
        so = int(input(f"Nhập phần tử thứ {i+1}: "))
        list_goc.append(so)
    list_binh_phuong = list(map(lambda x: x ** 2, list_goc))
    print("\nList ban đầu:", list_goc)
    print("List sau khi bình phương:", list_binh_phuong)
xu_ly_list_voi_map_lambda()