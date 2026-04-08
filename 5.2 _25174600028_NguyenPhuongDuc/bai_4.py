lst = []
while True:
    val = int(input("Nhập số (nhập 0 để dừng): "))
    if val == 0:
        break
    lst.append(val)
lst_4a = lst.copy()
lst_4a = [1,2,3] + lst_4a + [1,2,3]  # Đầu và cuối
if len(lst_4a) >= 4:
    lst_4a = lst_4a[:4] + [1,2,3] + lst_4a[4:] # Vị trí thứ 5
print("4a. Chèn [1,2,3]:", lst_4a)
k = int(input("Nhập vị trí k cần xóa (1-based): "))
lst_4b = lst.copy()
if 1 <= k <= len(lst_4b):
    lst_4b.pop(k-1)
print("Sau khi xóa phần tử thứ k:", lst_4b)
print(" Tăng dần:", sorted(lst))
print(" Giảm dần:", sorted(lst, reverse=True))