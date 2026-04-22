n = int(input("Nhập số n: "))

fibonacci = [0, 1] + [0 for _ in range(n-1)]
[fibonacci.__setitem__(i, fibonacci[i-1] + fibonacci[i-2]) for i in range(2, n+1)]

print(", ".join(str(so) for so in fibonacci))