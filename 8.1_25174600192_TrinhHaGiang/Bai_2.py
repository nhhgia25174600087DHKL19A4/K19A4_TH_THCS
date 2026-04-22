def day_fibonacci():
    a, b = 0, 1
    
    print("Dãy Fibonacci (không quá 20 số hạng):")
    
    for i in range(20):
        print(a, end=" ")
        a, b = b, a + b
day_fibonacci()
