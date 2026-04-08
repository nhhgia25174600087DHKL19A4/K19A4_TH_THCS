n=int(input("Nhập n:"))
x=[]
for i in range(1,n+1):
    x.append(i)
a=[]
for i in x:
    b=0
    for j in range(1,i+1):
        if i % j==0:
            b += 1
    if b == 2:
        a.append(i)
c=[]
for i in x:
    S=0
    for j in range (1,i):
        if i%j==0:
            S +=j
    if S == i:
        c.append(i)
print("Số nguyên tố:",a)
print("Số hoàn hảo:",c)