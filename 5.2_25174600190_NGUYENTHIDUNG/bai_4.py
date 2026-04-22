a = []
while True:
    val = int(input("Nhập số (0 để dừng): "))
    if val == 0:
        break
    a.append(val)
#a
sub = [1, 2, 3]
a = sub + a                         
a = a + sub                         
if len(a) >= 5:
    a[4:4] = sub                    
print("Danh sách sau khi chèn [1,2,3]:", a)
# b
k = int(input("Nhập vị trí k cần xóa (bắt đầu từ 0): "))
if 0 <= k < len(a):
    a.pop(k)
    print(f"Danh sách sau khi xóa vị trí {k}:", a)
# c
a.sort()
print("Sắp xếp tăng dần:", a)
a.sort(reverse=True)
print("Sắp xếp giảm dần:", a)