def luythua():
    x = int(input('Nhập số x = '))
    n = int(input('Nhập số mũ n = '))
    ket_qua = 1
    for i in range(n):
        ket_qua = ket_qua * x    
    print('Lũy thừa của', x, 'mũ', n, '=', ket_qua)
    return
luythua()