def fibonacci():
    a = 0
    b = 1
    print("Dãy Fibonacci (tối đa 20 số):")
    print(a, end=" ")
    print(b, end=" ")
    for i in range(18):  
        c = a + b
        print(c, end=" ")
        a = b
        b = c
fibonacci()