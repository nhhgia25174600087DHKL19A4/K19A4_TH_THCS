def tao_ds():
    n = int(input("Nhập số phần tử n: "))
    ds = []

    for i in range(n):
        x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
        ds = ds + [x]

    return ds


a = tao_ds()

kt = list(map(lambda t: True if t % 2 == 0 else False, a))

print("Danh sách:", a)
print("Kết quả:", kt)