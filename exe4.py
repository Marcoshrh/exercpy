matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for a in range(0, 5):
    for b in range(0, 5):
        matriz[a][b] = int(input(f'Digite um valor para [{a}, {b}]:'))
print('+=' * 30)
for a in range(0, 5):
    for b in range(0, 5):
        print(f'[{matriz[a][b]:^5}]', end=' ')
    print()




