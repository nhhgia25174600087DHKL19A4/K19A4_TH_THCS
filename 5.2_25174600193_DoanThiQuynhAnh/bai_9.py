a= list(map(int, input("Nhap cac so: ").split()))

for x in a:
    assert x % 2 == 0

print("Tat ca cac so deu la so chan")