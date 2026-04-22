def tinh(a, b):
    print("Cong:", a + b)
    print("Tru:", a - b)
    print("Nhan:", a * b)
    if b != 0:
        print("Chia:", a / b)
a = int(input("a: "))
b = int(input("b: "))
tinh(a, b)