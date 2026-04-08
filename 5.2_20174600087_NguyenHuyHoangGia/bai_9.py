n = int(input("Nhập số lượng phần tử: "))
a = []
for i in range(n):
    val = int(input("Nhập số: "))
    assert val % 2 == 0, "Nhập lại"
    a.append(val)
print("Danh sách toàn số chẵn của bạn là:", a)