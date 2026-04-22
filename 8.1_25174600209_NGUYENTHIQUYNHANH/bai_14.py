def bai_14():
    print("--- Chương trình tính bình phương bằng Map & Lambda ---")
    n = int(input("Nhập số lượng phần tử n: "))
    lst = []
    for i in range(n):
        so = int(input("Nhập phần tử thứ {}: ".format(i + 1)))
        lst.append(so)
    print("\nDanh sách gốc:", lst)
    lst_binh_phuong = list(map(lambda x: x**2, lst))
    print("Danh sách bình phương:", lst_binh_phuong)
bai_14()