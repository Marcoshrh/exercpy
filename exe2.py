num = [[], []]
for c in range(1, 10):
    valor = int(input("Digite um número:"))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f"Os números digitados são : {num}, separados em pares e ímpares, respectivamente ")
