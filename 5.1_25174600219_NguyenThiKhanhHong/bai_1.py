n=int(input("Nhập n:"))
m=int(input("Nhập m:"))
x=[]
for i in range(1,n+1):
    x.append(i*i)
if m>=n:
    print(x)
else:
    print(x[:m])