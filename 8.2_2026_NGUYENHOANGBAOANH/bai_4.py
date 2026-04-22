def dao_nguoc_ds():
    ds = list(map(int, input("Nhập các số (cách nhau bằng dấu cách): ").split()))
    

    ds_dao = []
    for i in range(len(ds)-1, -1, -1):
        ds_dao.append(ds[i])
    
    print("Đảo ngược:", ds_dao)

dao_nguoc_ds()