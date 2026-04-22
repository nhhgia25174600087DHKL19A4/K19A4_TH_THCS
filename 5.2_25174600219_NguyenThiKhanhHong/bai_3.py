a = []
while True:
    n = int(input("Nhập số (nhập 0 để dừng): "))
    if n == 0:
        break
    a.append(n)
# a. 
b = [x for x in a if x > 0]
c = [x for x in a if x <= 0]
d = b + c
print("Danh sách sau khi đưa số dương lên đầu:", d)
# b. 
m = int(input("Nhập số m cần chèn: "))
d.insert(0, m)        
d.append(m)           
if len(d) >= 5:
    d.insert(4, m)      
print("Danh sách sau khi chèn m:", d)