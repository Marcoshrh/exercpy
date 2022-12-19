
n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
while n1 > n2:
    print("Digite primeiro o número menor depois o maior ")
    n1 = int(input("Digite um número:"))
    n2 = int(input("Digite outro número:"))


for i in range(n1, n2 + 1):
    if i >= 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
