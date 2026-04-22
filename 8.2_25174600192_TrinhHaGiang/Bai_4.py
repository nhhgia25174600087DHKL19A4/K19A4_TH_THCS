def dao_nguoc(ds):
    ds_moi = []
    for i in range(len(ds) - 1, -1, -1):
        ds_moi.append(ds[i])
    return ds_moi
def main():
    n = int(input("Nhap so luong phan tu: "))
    
    ds = []
    for i in range(n):
        x = int(input("Nhap phan tu thu " + str(i+1) + ": "))
        ds.append(x)
    ds_dao = dao_nguoc(ds)
    print("Danh sach ban dau:", ds)
    print("Danh sach dao nguoc:", ds_dao)
main()