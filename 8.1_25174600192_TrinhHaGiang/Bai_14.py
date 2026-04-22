def main():
    n = int(input("Nhap so luong phan tu: "))
    ds = []
    for i in range(n):
        x = int(input("Nhap phan tu thu " + str(i+1) + ": "))
        ds.append(x)
    ds_binh_phuong = list(map(lambda x: x * x, ds))
    
    print("Danh sach ban dau:", ds)
    print("Danh sach binh phuong:", ds_binh_phuong)
main()