def bai_4():
    n = int(input("Nhập số lượng phần tử: "))
    lst = []
    for i in range(n):
        lst.append(input("Nhập phần tử thứ {}: ".format(i+1)))
    print("Danh sách gốc:", lst)
    lst_dao_nguoc = lst[::-1]
    print("Danh sách sau khi đảo ngược:", lst_dao_nguoc)
bai_4()