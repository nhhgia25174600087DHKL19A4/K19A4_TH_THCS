def dao_nguoc(ds):
    return ds[::-1]
ds = list(map(int, input("Nhập các số : ").split()))
print("Đảo ngược:", dao_nguoc(ds))