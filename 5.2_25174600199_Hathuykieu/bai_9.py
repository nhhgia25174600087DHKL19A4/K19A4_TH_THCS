a = list(map(int, input("Nhập các số: ").split()))
for i in range(len(a)):
    assert a[i] % 2 == 0, "Có số lẻ!"
print("Tất cả các số đều là số chẵn")