def in_fibonacci():
    so_luong = 20
    so_truoc = 0
    so_sau = 1
    print("Dãy Fibonacci gồm", so_luong, "số hạng đầu tiên là:")
    print(so_truoc, so_sau, sep=", ", end="")
    for _ in range(2, so_luong):
        so_tiep_theo = so_truoc + so_sau
        print(", ", so_tiep_theo, sep="", end="")
        so_truoc = so_sau
        so_sau = so_tiep_theo
in_fibonacci()