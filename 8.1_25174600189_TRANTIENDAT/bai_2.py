def fibonacci():
    n = int(input("Nhập số lượng phần tử (<=20): "))
    
    if n <= 0 or n > 20:
        print("Nhập lại (0 < n <= 20)")
        return
    
    a, b = 0, 1
    
    print("Dãy Fibonacci:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci()