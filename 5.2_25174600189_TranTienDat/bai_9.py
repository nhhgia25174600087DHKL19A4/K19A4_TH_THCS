a = [int(input()) for _ in range(5)]

for x in a:
    assert x % 2 == 0

print("Tất cả đều là số chẵn")