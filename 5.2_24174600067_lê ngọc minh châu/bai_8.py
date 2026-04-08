n = int(input("Nhap n: "))
fibonacci  = [0,1]
for i in range(2, n+1):
    fibonacci  = fibonacci  + [fibonacci [i-1] + fibonacci [i-2]]
for i in range(len(fibonacci )):
    print(fibonacci [i], end=", ")