while True:
    n = int(input("Nhập n (n > 0): "))
    if n > 0:
        break
    print("Vui lòng nhập lại!")
s1 = 0
for i in range(1, n + 1):
    s1 += i**2
s2 = 0
i = 0
while i <= n:
    s2 += (2*i + 1)**3
    i += 1
s4 = 0
for i in range(1, n + 1):
    s4 += ((-1)**(i-1)) / i
print(f"S1 = {s1}")
print(f"S2 = {s2}")
print(f"S4 = {s4}")