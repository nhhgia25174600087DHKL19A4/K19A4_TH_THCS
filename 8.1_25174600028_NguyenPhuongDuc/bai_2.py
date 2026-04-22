def ham_fibonacci():
    a, b = 0, 1
    so_hang = 0
    print("dãy fibonacci ", end="")
    while so_hang < 20:
        print(a, end=" ")
        a, b = b, a + b
        so_hang += 1
    print()
ham_fibonacci()