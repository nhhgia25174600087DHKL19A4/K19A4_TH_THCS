while True:
    n=int(input("Nhập n:"))
    m=int(input("Nhập m:"))
    if 0<m<n:
        break
    else:
        print("Nhập sai,nhập lại!")
x=[]
for i in range(m,n+1,2):
    x.append(i)
S=0
for i in x:
    S=S+i
print("Danh sách:",x)
print("Tổng là:",S)