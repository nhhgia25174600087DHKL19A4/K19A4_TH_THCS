n = int(input("Nhập n: "))
a = []
for i in range(n):
    x = int(input("Nhập phần tử thứ " + str(i+1) + ": "))
    a.append(x)
m = int(input("Nhập m: "))    
if m >= n:
    print("Danh sách rỗng []")
else:
    print("Kết quả:", a[m-1:])        