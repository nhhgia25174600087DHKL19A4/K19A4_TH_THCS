import math
while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("Vui lòng nhập n > 0!")

# --- Cách 1: Sử dụng vòng lặp FOR ---
print("\n--- Kết quả dùng vòng lặp FOR ---")
s1 = sum(i**2 for i in range(1, n + 1))
s2 = sum((2*i + 1)**3 for i in range(0, n + 1)) # từ 1^3 đến (2n+1)^3
s3 = sum((2*i)**4 for i in range(1, n + 1))
s4 = sum(((-1)**(i-1)) / i for i in range(1, n + 1))
s5 = sum(1 / (i * (i + 1)) for i in range(1, n + 1))
s6 = sum(1 / math.sqrt(i) for i in range(2, n + 1)) + (1/math.sqrt(2) if n>=2 else 0) # Bắt đầu từ 1/√2

print(f"S1 = {s1}\nS2 = {s2}\nS3 = {s3}\nS4 = {s4}\nS5 = {s5}\nS6 = {s6}")

# --- Cách 2: Sử dụng vòng lặp WHILE ---
print("\n--- Kết quả dùng vòng lặp WHILE ---")
w_s1, w_s2, w_s3, w_s4, w_s5, w_s6 = 0, 0, 0, 0, 0, 0
i = 1
while i <= n:
    w_s1 += i**2
    w_s3 += (2*i)**4
    w_s4 += ((-1)**(i-1)) / i
    w_s5 += 1 / (i * (i + 1))
    if i >= 2:
        w_s6 += 1 / math.sqrt(i)
    i += 1
j = 0
while j <= n:
    w_s2 += (2*j + 1)**3
    j += 1

print(f"S1 = {w_s1}\nS2 = {w_s2}\nS3 = {w_s3}\nS4 = {w_s4}\nS5 = {w_s5}\nS6 = {w_s6}")