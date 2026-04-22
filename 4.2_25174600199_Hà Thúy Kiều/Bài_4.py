chu = ["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]
n = int(input("Nhập số: "))
res = ""
while n > 0:
    d = n % 10
    res = chu[d] + " " + res
    n //= 10
print("Kết quả:", res.strip())