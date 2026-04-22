def fibonacci():
    a= 0
    b = 1
    so_dem = 0
    while so_dem < 20:
        print(a,end = " ")
        a,b=b,a+b
        so_dem += 1
fibonacci()