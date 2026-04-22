def ham():
    lst = [int(x) for x in input("Nhập các phần tử của list (cách nhau bởi khoảng trắng): ").split()]    
    lst_binh_phuong = list(map(lambda x: x**2, lst))
    print("List bình phương:", lst_binh_phuong)
ham()