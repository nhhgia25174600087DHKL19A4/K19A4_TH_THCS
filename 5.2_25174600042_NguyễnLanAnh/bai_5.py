A = [] 
so = 1

while len(A) < 1000:
    if so % 7 != 0:
        A.append(so)
    so = so + 1
    if so > 99999:
        break

print("Đã lấy xong 1000 số ")
print("3 số đầu tiên là:", A[0], A[1], A[2])