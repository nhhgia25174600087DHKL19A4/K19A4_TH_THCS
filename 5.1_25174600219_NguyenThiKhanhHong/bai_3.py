while True:
    n=int(input("Nhập n:"))
    m=int(input("Nhập m:"))
    if 0<m<n:
        break
    else:
        print("Nhập sai,nhập lại!")
a=list(range(m,n+1))
b=list(filter(lambda x:x%2==0,a ))
print("Các số chẵn là:",b)