n = int(input("Nhập n: "))
a = [0]*n
for i in range(n):
    a[i] = int(input("Nhập phần tử thứ " + str(i) + ": "))
chan = [0]*n
le = [0]*n
nc = 0
nl = 0
for i in range(n):
    if a[i] % 2 == 0:
        chan[nc] = a[i]
        nc += 1
    else:
        le[nl] = a[i]
        nl += 1
print("Số chẵn:", end=" ")
for i in range(nc):
    print(chan[i], end=" ")
print()
print("Số lẻ:", end=" ")
for i in range(nl):
    print(le[i], end=" ")
print()
t_chan = tuple(chan[:nc])
t_le = tuple(le[:nl])
print("Tuple số chẵn:", t_chan)
print("Tuple số lẻ:", t_le)