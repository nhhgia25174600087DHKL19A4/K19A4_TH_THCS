while True:
    m = int(input("Nhập m (m > 0): "))
    n = int(input("Nhập n (n > m): "))
    if 0 < m < n:
        break
    print("Vui lòng nhập lại thỏa mãn 0 < m < n!")
tuple_goc = tuple(range(m, n + 1))
vi_tri_giua = len(tuple_goc) // 2
tp1 = tuple_goc[:vi_tri_giua]
tp2 = tuple_goc[vi_tri_giua:]
print("Tuple 1 (nửa đầu):", tp1)
print("Tuple 2 (nửa cuối):", tp2)