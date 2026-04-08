n = int(input("Nhập n: "))
m = [0, 1]
for i in range(2, n + 1):
    m.append(m[i-1] + m[i-2])
output = ", ".join([str(x) for x in m[:n+1]])
print(output)