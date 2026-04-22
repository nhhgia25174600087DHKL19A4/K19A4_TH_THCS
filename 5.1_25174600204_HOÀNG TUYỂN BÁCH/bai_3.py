
while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    
    if 0 < m < n:
        break
    else:
        print("Lỗi, Yêu cầu 0 < m < n. Nhập lại.")
a = []
for i in range(m, n + 1):
    a.append(i)
even_list = []
for x in a:
    if x % 2 == 0:
        even_list.append(x)
print("Danh sách ban đầu:", a)
print("Các số chẵn:", even_list)